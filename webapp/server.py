from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import threading
import time
import paho.mqtt.client as mqtt

RSU_BROKER_IP = "192.168.98.11"  # IP address of the MQTT broker
BROKER_PORT = 1883
MQTT_TOPICS = ["vanetza/announce", "vanetza/parking_status"]

clients = []

class SSEHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/events':
            self.send_response(200)
            self.send_header('Content-type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()

            clients.append(self)
            try:
                while True:
                    time.sleep(5)
            except Exception as e:
                print(f"Error in SSEHandler: {e}")
            finally:
                clients.remove(self)
        else:
            super().do_GET()

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with code {rc}")
    for topic in MQTT_TOPICS:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    if msg.topic == "vanetza/parking_status":
        data = json.loads(msg.payload.decode())
        notify_clients(data)

def notify_clients(data):
    for client in clients:
        try:
            client.wfile.write(f"data: {json.dumps(data)}\n\n".encode('utf-8'))
        except Exception as e:
            print(f"Error notifying client: {e}")

def start_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SSEHandler)
    print("HTTP server running on port 8080")
    httpd.serve_forever()

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(RSU_BROKER_IP, BROKER_PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    threading.Thread(target=start_server).start()
    threading.Thread(target=start_mqtt_client).start()
