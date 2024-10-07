from network import LoRa
import machine
import struct
import socket
import pycom
import time
import json
import os

# ----------------------------------
# Protocolos:

# https://docs.python.org/3/library/struct.html
PROTOCOLS = {
    0x0: '!BBH8s8s',             # ICMP Request: id, timeout, size, MAC src, MAC dest
    0x1: '!BBH8s8s',             # ICMP Reply: id, timeout, size, MAC dst, MAC src
    0x2: '!BBH8s8sB',            # TCP Syn: id, timeout, size, MAC src, MAC dest, synID
    0x3: '!BBH8s8sBB',           # TCP SynAck: id, timeout, size, MAC src, MAC dest, synID, ackID   
    0x4: '!BBQ8s8sB%ds',         # TCP Ack: id, timeout, size, MAC src, MAC dest, ackID, data
    0x5: '!BBH8s8sB',            # TCP Fin: id, timeout, size, MAC src, MAC dest, finID -> If it is ackID + 1 from ACK then close connection and its ok, if it's different then it's wrong and its tcp failed
    0x6: '!BBH8s8s7s',           # ARP Request: id, timeout, size, MAC src, MAC dest
    0x7: '!BBH8s8s7s',           # ARP Response: id, timeout, size, MAC dst, MAC src
}

HEADER_PROTOCOLS = {
    0x0: 16,
    0x1: 16,
    0x2: 17,
    0x3: 18,
    0x4: 17,
    0x5: 17,
}

COLORS = {
    "red": 0xff0000,
    "orange": 0xffa500,
    "yellow": 0xffff00,
    "green": 0x00ff00,
    "cyan": 0x00ffff,
    "blue": 0x0000ff,
    "purple": 0x800080,
    "white": 0xffffff,
    "off": 0x000000,
}

# ----------------------------------

# format of log message with time and packet information
def log_message(message,arg1=None,arg2=None):
    log = "{}:{}:{}\t>\t{}".format(
        time.localtime()[3],
        time.localtime()[4],
        time.localtime()[5],
        message,
    )
    if arg1 and arg2:
        log += ":\t{}\tand\t{}".format(
            arg1,
            arg2,
        )
    elif arg1 and not arg2:
        log += ":\t{}".format(
            arg1,
        )

    print(log)

# ----------------------------------

def load_config() -> dict:
    # the config.json file is loaded to the device as part of the build process
    with open('/flash/gateway_config.json','r') as fp:
        buf = json.load(fp)
    return buf

def wifi_connect(wifi_config: dict, retries: int = None) -> WLAN:
    if retries is not None and retries <= 0:
        raise Exception('All WiFi connection attempts failed')

    print('Connecting to WiFi...')
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(
        ssid=wifi_config['ssid'],
        auth=(WLAN.WPA2, wifi_config['password']),
        timeout=5000
    )

    try:
        while not wlan.isconnected():
            machine.idle()
        print("Connected to WiFi\n")
        pycom.rgbled(0x103300)
    except:
        print("Error connecting to WiFi")
        pycom.rgbled(0xff0000)

        # Wait 5 seconds and try again
        time.sleep(5)
        wifi_connect(wifi_config, retries - 1 if retries is not None else None)
    
    return wlan


# ----------------------------------
# LoRa functions:

def get_lora_socket() -> (LoRa, socket.socket):
    # TODO: we should be able to change the frequency and the bandwidth
    
    # Lora config:
    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, sf=7)

    # Socket config:
    lora_socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    lora_socket.setblocking(False)

    log_message("Lora status", lora.stats())

    return lora, lora_socket

# ----------------------------------
# MQTT functions:

def get_mqtt_client(mqtt_config: dict, sub_cb: function) -> MQTTClient:
    mqtt_client = MQTTClient(
        mqtt_config["client_id"],
        mqtt_config["server"],
        port=mqtt_config["port"]
    )
    # the callback is called when a message is received
    # mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    return mqtt_client

# ----------------------------------

buffer = []

# ----------------------------------
# Protocol functions:

# parse packet depending on protocol and it's data, 
# if param is true then it's a tcp packet
def parse_packet(packet):
    print("PACKET: ", packet)
    id = struct.unpack('!B', packet[:1])[0]
    print(id)

    if id not in PROTOCOLS:
        # raise Exception('Unknown protocol: ', id)
        return []

    if id == 0x4:
        size = struct.unpack('!Q', packet[2:10])[0] - HEADER_PROTOCOLS[id]
        expected_size = struct.calcsize(PROTOCOLS[id] % size)
        if len(packet) < expected_size:
            log_message("ERROR: ", "Packet size is smaller than expected.")
            return []
        return list(struct.unpack(PROTOCOLS[id] % size, packet))

    return list(struct.unpack(PROTOCOLS[id], packet))


# build packet depending on protocol and it's data
def compose_packet(data, param=None):
    if data[0] not in PROTOCOLS:
        raise Exception('Unknown protocol: ', data[0])

    if param:
        return struct.pack(PROTOCOLS[data[0]] % param, *data)

    return struct.pack(PROTOCOLS[data[0]], *data)

def get_buffer():
    return buffer

# decreses timeout of each packet in buffer and discard if timeout is 0
def decrease_or_discard():
    # Alterei esta função porque o main não deve 
    # ter capacidade de alterar o buffer

    for packet in buffer:
        packet[1] -= 1
        if packet[1] <= 0:
            buffer.remove(packet)

# check if a packet with the same params exists in buffer, and return it
def exist_in_buffer(params):
    checkParams = []

    for packet in buffer:
        for param in params:
            if param[0] < len(packet):
                if packet[param[0]] == param[1]:
                    checkParams.append(True)
                    if len(checkParams) == len(params):
                        return packet

        checkParams = []

    return None


def discard_from_buffer(params):    # Discard all packets from buffer that match params
    for param in params:
        packet = exist_in_buffer(param)
        if packet:
            buffer.remove(packet)
    return buffer


def icmp_request(src, dest, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    packet = [0x0, 20, 16, src, dest]
    buffer.append(packet + [time.time()])

    request = compose_packet(packet)
    s.send(request)
    log_message("icmp request", packet)


def icmp_reply(src, dest, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    packet = [0x1, 20, 16, src, dest]
    # buffer.append(packet + [time.time()])

    reply = compose_packet(packet)
    s.send(reply)
    log_message("icmp reply", packet)


def arp_request(src, device_name, s):
    if len(src) != 8:
        raise Exception('Invalid MAC address')

    packet = [0x6, 20, 16, src,
              b'\xff\xff\xff\xff\xff\xff\xff\xff', device_name]    # Broadcast
    buffer.append(packet + [time.time()])

    request = compose_packet(packet)
    s.send(request)
    log_message("arp request", packet)


def arp_response(src, dest, device_name, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    packet = [0x7, 20, 16, src, dest, device_name]
    # buffer.append(packet + [time.time()])

    reply = compose_packet(packet)
    s.send(reply)
    log_message("arp response", packet)


def tcp_syn(src, dest, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    synID = ord(os.urandom(1))

    packet = [0x2, 10, 17, src, dest, synID]
    buffer.append(packet + [time.time()])

    syn = compose_packet(packet)
    s.send(syn)
    log_message("tcp syn", packet)


def tcp_synack(src, dest, synID, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    ackID = synID + 1                 # TCP Behaviour -> ackID = synID + 1
    synID = ord(os.urandom(1))

    packet = [0x3, 10, 18, src, dest, synID, ackID]
    buffer.append(packet + [time.time()])

    synack = compose_packet(packet)
    s.send(synack)
    log_message("tcp synack", packet)


def tcp_ack(src, dest, synID, data, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    ackID = synID + 1                   # TCP Behaviour -> ackID = synID + 1
    size = len(data)

    packet = [0x4, 10, size + HEADER_PROTOCOLS[0x4], src, dest, ackID, data]
    buffer.append(packet + [time.time()])

    ack = compose_packet(
        packet,size
    )
    s.send(ack)
    log_message("tcp ack", packet)


def tcp_fin(src, dest, ackID, s):
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')

    finID = ackID + 1

    packet = [0x5, 10, 17, src, dest, finID]
    buffer.append(packet + [time.time()])

    fin = compose_packet(packet)
    s.send(fin)
    log_message("tcp fin", packet)


def discard_tcp(src, dest):     # Discard all TCP packets from src to dest
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')
    
    discard_from_buffer([
        [(0,0x2),(3,src),(4,dest)],
        [(0,0x3),(3,src),(4,dest)],
        [(0,0x4),(3,src),(4,dest)],
        [(0,0x5),(3,src),(4,dest)],
    ])


def discard_arp(src, dest):     # Discard all ARP packets from src to dest
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')
    
    discard_from_buffer([
        [(0,0x6),(3,src),(4, b'\xff\xff\xff\xff\xff\xff\xff\xff')],
        [(0,0x7),(3,src),(4,dest)],
    ])


def discard_icmp(src, dest):     # Discard all ICMP packets from src to dest
    if len(src) != 8 or len(dest) != 8:
        raise Exception('Invalid MAC address')
    
    discard_from_buffer([
        [(0,0x0),(3,src),(4,dest)],
        [(0,0x1),(3,src),(4,dest)],
    ])
