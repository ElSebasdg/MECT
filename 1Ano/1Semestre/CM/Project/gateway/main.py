import pycom
import lib.utils as utils
import time
import json
from network import LoRa
import _thread


def sub_cb(topic, msg):
    # This callback is called when a mqtt message is received
    print(topic)
    print(msg)

    # Topic is something like: cm-project/controller/device_name/{led_status, color}
    # msg is something like: 0 or 1 or cyan or green or purple or white...

    topic = topic.decode('utf-8')

    # Get the device name from the topic
    device_name = topic.split('/')[2]

    # Get the message from the topic
    message = topic.split('/')[3]

    # Get the message value from the msg
    message_value = msg.decode('utf-8')

    # Create the message to send to the node
    message_to_send = {
        "device": device_name,
        "message": message + '|' + message_value
    }

    # print(message_to_send)

    # Add the message to the messages list in first position
    messages.append(message_to_send)
    # print(messages)


pycom.heartbeat(False)

# Load config
conf = utils.load_config()

# Connect to wifi
if "network" not in conf:
    print("[ERROR] WIFI config missing")
    exit(1)

wlan = utils.wifi_connect(conf["network"], 2)

# LoRa client
lora, lora_socket = utils.get_lora_socket()

board = {
    "name": conf["device_name"],
    "mac": lora.mac(),
}

# MQTT client
if "mqtt" not in conf:
    print("[ERROR] MQTT config missing")
    exit(1)

mqtt_client = utils.get_mqtt_client(conf["mqtt"], sub_cb)
mqtt_client.set_callback(sub_cb)
mqtt_client.subscribe(topic=conf["mqtt"]["topics"]["subscribe"])

known_nodes = set()
active_nodes = set()
mac_to_devices = {}
arp_timeout = 60
keepalive = 23
packet_loss = 0

i = 0

messages = [
    {
        "device": "all",
        "message": "color|cyan",
    },
    {
        "device": "all",
        "message": "color|green",
    },
    {
        "device": "all",
        "message": "color|purple",
    },
    {
        "device": "all",
        "message": "color|white",
    },
    {
        "device": "all",
        "message": "status|0",
    }
]

next_message = None
info = None
messages_sent = 0

while True:
    try:
        if messages_sent == 50:
            print("THE END")
            break

        pycom.rgbled(0x00ff00)
        # utils.log_message("buffer", utils.get_buffer())

        print("NEXT: ", next_message)

        print("ACTIVE: ", active_nodes)

        # Scanning for new nodes
        if arp_timeout == 60:
            # _thread.start_new_thread(utils.arp_request, (board["mac"], board["name"], lora_socket))
            utils.arp_request(
                board["mac"], board["name"].encode('utf-8'), lora_socket
            )
            arp_timeout = 0

        # print("MESSAGES: ", messages)

        # Testing connectivity
        if keepalive == 30:
            keepalive = 0
            if len(known_nodes) > 0:
                for node in known_nodes:
                    if not utils.exist_in_buffer([(0, 0), [3, board["mac"]], (4, node)]):
                        # _thread.start_new_thread(utils.icmp_request, (board["mac"], node, lora_socket))
                        utils.icmp_request(
                            board["mac"], node, lora_socket
                        )

        # if there is a message send through tcp
        devices_to_mac = {v: k for k, v in mac_to_devices.items()}
        if next_message and len(active_nodes) > 0:
            if next_message["device"] == "all":
                # send to all active nodes
                for node in active_nodes:
                    if not utils.exist_in_buffer([(0, 0x2), (3, board["mac"]), (4, node)]):
                        # _thread.start_new_thread(utils.tcp_syn, (board["mac"], node, lora_socket))
                        utils.tcp_syn(
                            board["mac"], node, lora_socket
                        )
                        time.sleep(0.1)

            elif next_message["device"] in devices_to_mac:
                # send to specific node
                if not utils.exist_in_buffer([(0, 0x2), (3, board["mac"]), (4, devices_to_mac[next_message["device"]])]):
                    # _thread.start_new_thread(utils.tcp_syn, (board["mac"], devices_to_mac[next_message["device"]], lora_socket))
                    utils.tcp_syn(
                        board["mac"], devices_to_mac[next_message["device"]
                                                     ], lora_socket
                    )

        elif len(messages) > 0 and not next_message and len(active_nodes) > 0:
            # get next message
            next_message = messages.pop(0)
            print("MESSAGES", len(messages))
            # TODO: delete this TESTING ONLY
            messages.append(next_message)
            messages_sent += 1

        # Receive LoRa packets
        packet = lora_socket.recv(100)
        if packet:
            # packet is not empty

            data = utils.parse_packet(packet)

            # utils.log_message("receiver",data)

            if len(data) == 0:
                continue

            # check if ICMP Reply is correct
            if data[0] == 0x1 and data[4] == board["mac"] and data[3] in known_nodes:
                active_nodes.add(data[3])
                utils.discard_icmp(board["mac"], data[3])

            # check if ARP Reply is correct
            elif data[0] == 0x7 and data[4] == board["mac"]:
                known_nodes.add(data[3])
                # Unpack this to a string this is in bytes
                mac_to_devices[data[3]] = data[5].decode(
                    'utf-8').rstrip('\x00')
                utils.discard_arp(board["mac"], data[3])

            # synack
            elif data[0] == 0x2 and data[4] == board["mac"] and not utils.exist_in_buffer([(0, 3), (3, board["mac"]), (4, data[3]), (6, (data[5]+1))]):
                # _thread.start_new_thread(utils.tcp_synack, (board["mac"], data[3], data[5], lora_socket))
                utils.tcp_synack(
                    board["mac"], data[3], data[5], lora_socket
                )

            # ack
            elif data[0] == 0x3 and data[4] == board["mac"] and data[3] in active_nodes and next_message and not utils.exist_in_buffer([(0, 0x4), (3, board["mac"]), (4, data[3]), (5, data[5]+1), (6, next_message["message"])]):
                # Check if ackID from TCP SynAck is synID from TCP Syn + 1
                syn = utils.exist_in_buffer([
                    (0, 0x2), (3, board["mac"]), (4, data[3]), (5, data[6]-1)
                ])
                if syn:
                    # _thread.start_new_thread(
                    #     utils.tcp_ack, (board["mac"], data[3], data[5], next_message["message"], lora_socket)
                    # )
                    utils.tcp_ack(
                        board["mac"], data[3], data[5], next_message["message"], lora_socket
                    )

                    print("---------------------------------")
                    print("SENDING: ", next_message["message"])
                    print("---------------------------------")

                    # utils.log_message("tcp ack", mac_to_devices[data[3]])

                    # We received a response, so we can calculate the rtt and the throughput
                    # syn[6] is the timestamp of the tcp syn
                    rtt = time.time() - syn[6]
                    # syn[2] is the number of bits sent and data[2] is the number of bits received
                    throughput = (syn[2] + data[2]) / rtt

                    # This RTT and throughput represents the communication between the gateway and the node

                    # send these metrics to the mqtt broker
                    mqtt_client.publish(
                        topic=conf["mqtt"]["topics"]["publish"] + '/' + mac_to_devices[data[3]] + '/rtt', msg=str(rtt))
                    mqtt_client.publish(topic=conf["mqtt"]["topics"]["publish"] + '/' +
                                        mac_to_devices[data[3]] + '/throughput', msg=str(throughput))

            # fin
            elif data[0] == 0x4 and data[4] == board["mac"] and data[3] in active_nodes and not utils.exist_in_buffer([(0, 5), (3, board["mac"]), (4, data[3]), (5, (data[5]+1))]):
                # Check if the size and the message are the same
                if len(data[6]) == (data[2] - utils.HEADER_PROTOCOLS[0x4]):
                    # _thread.start_new_thread(utils.tcp_fin, (board["mac"], data[3], data[5], lora_socket))
                    utils.tcp_fin(
                        board["mac"], data[3], data[5], lora_socket
                    )
                    info = json.loads(data[6])
                    print("---------------------------------")
                    print("INFO: ", info)
                    print("---------------------------------")
                    # utils.log_message("tcp fin", json.loads(info))
                    # TODO: send status to broker
                    # {'color': 'cyan', 'status': 1, 'name': 'board14'}
                    mqtt_client.publish(topic=conf["mqtt"]["topics"]["publish"] + '/' +
                                        mac_to_devices[data[3]] + '/led_status', msg=str(info['status']))
                    mqtt_client.publish(topic=conf["mqtt"]["topics"]["publish"] +
                                        '/' + mac_to_devices[data[3]] + '/color', msg=str(info['color']))

                else:
                    # utils.log_message("tcp fin failed", data[6])
                    # send a fin packet with the wrong id so the node resends the packet
                    # this is just to avoid having to await for the timeout
                    # _thread.start_new_thread(utils.tcp_fin, (board["mac"], data[3], 0, lora_socket))
                    utils.tcp_fin(
                        board["mac"], data[3], 0, lora_socket
                    )

            elif data[0] == 0x5 and data[4] == board["mac"] and data[3] in active_nodes:
                # Check if ackID from TCP FinAck is finID from TCP Fin + 1
                ack = utils.exist_in_buffer([
                    (0, 0x4), (3, board["mac"]), (4, data[3]), (5, data[5]-1)
                ])
                if ack:
                    # utils.log_message("tcp session closed", board["mac"], data[3])
                    next_message = None

                    # We received a response, so we can calculate the rtt and the throughput
                    # ack[6] is the timestamp of the tcp ack
                    rtt = time.time() - ack[7]
                    # ack[2] is the number of bits sent and data[2] is the number of bits received
                    throughput = (ack[2] + data[2]) / rtt

                    # This RTT and throughput represents the communication between the gateway and the node

                    # send these metrics to the mqtt broker
                    mqtt_client.publish(
                        topic=conf["mqtt"]["topics"]["publish"] + '/' + mac_to_devices[data[3]] + '/rtt', msg=str(rtt))
                    mqtt_client.publish(topic=conf["mqtt"]["topics"]["publish"] + '/' +
                                        mac_to_devices[data[3]] + '/throughput', msg=str(throughput))
                else:
                    utils.log_message("tcp session failed",
                                      board["mac"], data[3])

                utils.discard_tcp(board["mac"], data[3])

        packet_loss, active_nodes = utils.decrease_or_discard(
            packet_loss, active_nodes)
        arp_timeout += 1
        keepalive += 1

        # send packet loss to mqtt broker
        mqtt_client.publish(topic=conf["mqtt"]["topics"]["publish"] +
                            '/' + board["name"] + '/packet_loss', msg=str(packet_loss))

        # O MQTT ainda não está na versão final,
        # mas vou deixar isto aqui para conseguir criar os dashboards

        # TODO: from time to time send the list of active nodes to the broker

        # Let's check if we are still connected to wifi
        if not wlan.isconnected():
            print("Disconnected from WiFi")
            pycom.rgbled(0xff0000)
            time.sleep(5)

            wlan = utils.wifi_connect(conf["network"], 5)

        # Let's check if we are still connected to mqtt
        if not mqtt_client.is_connected():
            print("Disconnected from MQTT")
            pycom.rgbled(0xff0000)
            time.sleep(5)

            mqtt_client = utils.get_mqtt_client(conf["mqtt"], sub_cb)
            mqtt_client.set_callback(sub_cb)
            mqtt_client.subscribe(topic=conf["mqtt"]["topics"]["subscribe"])

        mqtt_client.check_msg()

        pycom.rgbled(0xff00ff)
    except Exception as e:
        print(e)

    time.sleep(1)
