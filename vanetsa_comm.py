import paho.mqtt.client as mqtt
import json
import time

# Configuration for MQTT brokers
RSU_BROKER_IP = "192.168.98.11"   # IP address of the RSU (broker for all OBUs)
BROKER_PORT = 1883                # Standard MQTT port

# Topics for communication
TOPIC_ANNOUNCE = "vanetza/announce"
TOPIC_PARKING_STATUS = "vanetza/parking_status"

# Define station IDs
RSU_ID = 1
OBU_IDS = [3, 4, 5, 6]

# Create announcement message
def create_announce_message(station_id, station_type):
    return {
        "station_id": station_id,
        "station_type": station_type,
        "message": "Announce presence",
        "timestamp": time.time()
    }

# Create parking status message
def create_parking_status_message(station_id, status):
    return {
        "station_id": station_id,
        "status": status,
        "timestamp": time.time()
    }

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker with code {rc}")
        client.subscribe(TOPIC_ANNOUNCE)
        client.subscribe(TOPIC_PARKING_STATUS)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    data = json.loads(msg.payload.decode())
    if msg.topic == TOPIC_PARKING_STATUS:
        handle_parking_status(data)

def handle_parking_status(data):
    station_id = data.get("station_id")
    status = data.get("status")
    if status == "parking_request":
        print(f"Station {station_id} requests to park. Granting permission.")
        response = create_parking_status_message(RSU_ID, "parking_granted")
        client.publish(TOPIC_PARKING_STATUS, json.dumps(response))
    elif status == "parking_granted":
        print(f"Parking granted for station {station_id}.")
    else:
        print(f"Unknown status: {status}")

# Instantiate MQTT client
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"Attempting to connect to {RSU_BROKER_IP}:{BROKER_PORT}")
    client.connect(RSU_BROKER_IP, BROKER_PORT, 60)
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

client.loop_start()

try:
    while True:
        for obu_id in OBU_IDS:
            announce_msg = create_announce_message(obu_id, 5)
            client.publish(TOPIC_ANNOUNCE, json.dumps(announce_msg))
            print(f"Announced presence for OBU {obu_id}")

            parking_request_msg = create_parking_status_message(obu_id, "parking_request")
            client.publish(TOPIC_PARKING_STATUS, json.dumps(parking_request_msg))
            print(f"Parking request sent for OBU {obu_id}")

        time.sleep(10)

except KeyboardInterrupt:
    print("Stopping script.")
    client.loop_stop()
    client.disconnect()
