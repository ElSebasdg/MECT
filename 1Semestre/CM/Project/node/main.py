import json
import time
import pycom
import lib.utils as utils
import _thread

# COM6

pycom.heartbeat(False)

lora, lora_socket = utils.get_lora_socket()

# caracteristics of own device
board = {
    "name": "board14",
    "mac": lora.mac(),
    "gateway": None,
    "status": 1,
    "color": "red",
}

pycom.rgbled(utils.COLORS[board["color"]])

info_interval = 17
info_to_send = {"name": board["name"], "status": board["status"], "color": board["color"]}

while True:
    utils.log_message("buffer", utils.get_buffer())

    # Openning a session with the gateway, to send its information
    if info_interval == 10:
        if board["gateway"]:
            # _thread.start_new_thread(
            #     utils.tcp_syn, (board["mac"], board["gateway"], lora_socket)
            # )
            utils.tcp_syn(board["mac"], board["gateway"], lora_socket)
        info_interval = 0
    else:
        info_interval += 1

    packet = lora_socket.recv(100)

    if packet:
        
        data = utils.parse_packet(packet)

        utils.log_message("receiver", data)

        if len(data) == 0:
            print("break")
            continue

        # ICMP
        if data[0] == 0x0 and not utils.exist_in_buffer([(0, 0x1), [3, board["mac"]], (4, data[3])]):
            # _thread.start_new_thread(utils.icmp_reply, (board["mac"], data[3], lora_socket))
            utils.icmp_reply(board["mac"], data[3], lora_socket)

        # ARP
        elif data[0] == 0x6 and not utils.exist_in_buffer([(0, 0x7), [3, board["mac"]], (4, data[3])]):
            # _thread.start_new_thread(utils.arp_response, (board["mac"], data[3], board["name"], lora_socket))
            utils.arp_response(board["mac"], data[3], board["name"].encode('utf-8'), lora_socket)
            board["gateway"] = data[3]
        
        # TCP
        elif data[0] == 0x2 and data[4] == board["mac"] and not utils.exist_in_buffer([(0, 3), (3, board["mac"]), (4, data[3]), (6, (data[5]+1))]):
            # _thread.start_new_thread(utils.tcp_synack, (board["mac"], data[3], data[5], lora_socket))
            utils.tcp_synack(board["mac"], data[3], data[5], lora_socket)
        
        # ack
        elif data[0] == 0x3 and data[4] == board["mac"] and not utils.exist_in_buffer([(0, 0x4), (3, board["mac"]), (4, data[3]), (5, data[5]+1), (6, json.dumps(info_to_send))]):
            # Check if ackID from TCP SynAck is synID from TCP Syn + 1
            syn = utils.exist_in_buffer([
                (0, 0x2), (3, board["mac"]), (4, data[3]), (5, data[6]-1)
            ])
            if syn:
                # _thread.start_new_thread(
                #     utils.tcp_ack, (board["mac"], data[3], data[5], json.dumps(info_to_send), lora_socket)
                # )
                info_to_send = {"name": board["name"],"status": board["status"],"color": board["color"]}
                utils.tcp_ack(
                    board["mac"], data[3], data[5],
                    json.dumps(info_to_send),
                    lora_socket
                )
        
        elif data[0] == 0x4 and data[4] == board["mac"] and not utils.exist_in_buffer([(0, 5), (3, board["mac"]), (4, data[3]), (5, (data[5]+1))]):
            # Check if the size and the message are the same
            if len(data[6]) == (data[2] - utils.HEADER_PROTOCOLS[0x4]):
                # _thread.start_new_thread(utils.tcp_fin, (board["mac"], data[3], data[5], lora_socket))
                utils.tcp_fin(board["mac"], data[3], data[5], lora_socket)
                message = data[6].decode('utf-8').split("|")
                if message[0] == "status" and (message[1] == "0" or message[1] == "1"):
                    board["status"] = int(message[1])
                    if board["status"] == 0:
                        pycom.rgbled(utils.COLORS["off"])
                elif message[0] == "color" and message[1] in utils.COLORS:
                    if board["status"] == 0:
                        board["status"] = 1
                    board["color"] = message[1]
                    pycom.rgbled(utils.COLORS[board["color"]])
                info_interval = 10 # this will force the sending of a status update
            else:
                utils.log_message("tcp ack failed", board["mac"], data[3])
                # _thread.start_new_thread(utils.tcp_fin, (board["mac"], data[3], 0, lora_socket))
                utils.tcp_fin(board["mac"], data[3], 0, lora_socket)
        
        elif data[0] == 0x5 and data[4] == board["mac"]:
            # Check if the ackID is the same
            if utils.exist_in_buffer([(0, 0x4), (3, data[4]), (4, data[3]), (5, data[5]-1)]):
                utils.log_message("tcp session closed", board["mac"], data[3])
            else:
                utils.log_message("tcp session failed", board["mac"], data[3])
            utils.discard_tcp(board["mac"], data[3])

    utils.decrease_or_discard()
    time.sleep(1)