import time
import json
import paho.mqtt.client as mqtt
import datetime

# Broker details
BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

# MQTT callback for connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("vanetza/parking_status")  # Subscribe to parking status
    client.subscribe("obu/to/rsu")  # Subscribe to messages from OBU to RSU
    client.subscribe("rsu/to/obu")  # Subscribe to messages from RSU to OBU

# MQTT callback for incoming messages
def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    topic = msg.topic
    
    if topic == "obu/to/rsu":
        print(f"Received message from OBU: {message}")
        process_obu_message(client, message)
    elif topic == "rsu/to/obu":
        print(f"Received message from RSU: {message}")
        process_rsu_message(client, message)
    else:
        print(f"Received message on {topic}: {message}")

def process_obu_message(client, message):
    # Example: RSU responds to OBU
    response = {
        "response": "Acknowledged by RSU",
        "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
    }
    client.publish("rsu/to/obu", json.dumps(response))
    print(f"RSU sent response: {response}")

def process_rsu_message(client, message):
    # Example: OBU processes message from RSU
    print(f"OBU processing message: {message}")

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
        print(f"OBU sent message: {message}")
        
        # Send a message to RSU
        rsu_message = {
            "obu_id": obu_id,
            "message": "OBU at new location",
            "location": {"lat": lat, "lon": lon},
            "timestamp": timestamp
        }
        client.publish("obu/to/rsu", json.dumps(rsu_message))
        
        idx = (idx + 1) % len(animation_path)
        time.sleep(2)  # Adjust the sleep time for desired speed

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, BROKER_PORT, 60)

simulate_obu_movements(client, 1, "vanetza/parking_status")
