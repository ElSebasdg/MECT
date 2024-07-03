import time
import json
import paho.mqtt.client as mqtt
import random
import datetime

BROKER_IP = "192.168.98.11"  # Replace with the IP of your RSU or MQTT broker
BROKER_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("vanetza/parking_status")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print(f"Received message on {msg.topic}: {message}")

def get_university_aveiro_coordinates():
    # Specific coordinates within the University of Aveiro campus
    return [
        [40.6304, -8.6573],  # Campus Center
        [40.6287, -8.6581],  # Library
        [40.6315, -8.6589],  # Main Entrance
        [40.6322, -8.6570],  # Parking Lot A
        [40.6292, -8.6550],  # Parking Lot B
    ]

def simulate_obu_movements(client, obu_id, topic):
    coordinates = get_university_aveiro_coordinates()
    while True:
        # Randomly select a location from the predefined list
        location = random.choice(coordinates)
        timestamp = datetime.datetime.utcnow().isoformat() + 'Z'
        message = {
            "station_id": obu_id,
            "status": "parking_request",
            "latitude": location[0],
            "longitude": location[1],
            "timestamp": timestamp
        }
        client.publish(topic, json.dumps(message))
        print(f"Sent message: {message}")
        time.sleep(random.randint(5, 15))  # Random sleep interval

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, BROKER_PORT, 60)

# Start movement simulation for each OBU
ob1_topic = "vanetza/parking_status"
simulate_obu_movements(client, 1, ob1_topic)
