import time
import json
import paho.mqtt.client as mqtt
import datetime

BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("vanetza/parking_status")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print(f"Received message on {msg.topic}: {message}")

def simulate_obu_movements(client, obu_id, topic):
    animation_path = [
        [40.6312, -8.6564],
        [40.6312, -8.6563],
        [40.6305, -8.6554],
        [40.6292, -8.6550],
        [40.6285, -8.6561],
        [40.6289, -8.6576],
        [40.6294, -8.6582],
        [40.6298, -8.6588],
        [40.6301, -8.6592],
        [40.6305, -8.6587],
        [40.6308, -8.6585],
        [40.6312, -8.6581],
        [40.6314, -8.6578],
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
        
        time.sleep(2)  # Adjust the sleep time for desired speed

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, BROKER_PORT, 60)

simulate_obu_movements(client, 1, "vanetza/parking_status")
