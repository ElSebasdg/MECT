from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import threading
import time
import random
import datetime
import paho.mqtt.client as mqtt

# MQTT Configuration
RSU_BROKER_IP = "192.168.98.11"  # IP address of the RSU
BROKER_PORT = 1883

# SSE clients
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
    client.subscribe("vanetza/announce")
    client.subscribe("vanetza/parking_status")

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")
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

def simulate_obu_movements(client, obu_id, topic):
    animation_path = [
        [40.6315, -8.6589],  # Main Entrance
        [40.6310, -8.6595],  # Near Library
        [40.6300, -8.6590],  # Middle of Rua de Santiago
        [40.6295, -8.6580],  # Near Cafeteria
        [40.6290, -8.6575],  # End of Rua de Santiago
    ]
    
    idx = 0
    while True:
        lat, lon = animation_path[idx]
        
        timestamp = datetime.datetime.utcnow().isoformat() + 'Z'
        message = {
            "station_id": obu_id,
            "status": "moving",
            "latitude": lat,
            "longitude": lon,
            "timestamp": timestamp
        }
        
        client.publish(topic, json.dumps(message))
        print(f"Sent message: {message}")
        
        idx = (idx + 1) % len(animation_path)
        
        time.sleep(random.randint(5, 15))

if __name__ == '__main__':
    threading.Thread(target=start_server).start()
    threading.Thread(target=start_mqtt_client).start()
