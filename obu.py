import time
import json
import paho.mqtt.client as mqtt
import datetime

BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

# Callback when the client connects
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("rsu/to/obu")  # Subscribe to responses from RSU

# Callback when a message is received
def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload)
        print(f"Received message on {msg.topic}: {message}")
    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload}")

    # Handle the response from RSU
    if msg.topic == "rsu/to/obu":
        print(f"RSU response received: {message}")

# Function to simulate OBU movements and send messages to RSU
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
        
        # Send message to RSU
        rsu_message = {
            "obu_id": obu_id,
            "message": "OBU at new location",
            "location": {"lat": lat, "lon": lon},
            "timestamp": timestamp
        }
        client.publish("obu/to/rsu", json.dumps(rsu_message))
        
        idx = (idx + 1) % len(animation_path)
        time.sleep(2)  # Adjust the sleep time for desired speed

# Initialize the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROKER_IP, BROKER_PORT, 60)

# Start the simulation in a non-blocking way
client.loop_start()
simulate_obu_movements(client, 1, "vanetza/parking_status")
