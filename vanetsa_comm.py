import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime, timezone

# Configuration for MQTT broker
RSU_BROKER_IP = "192.168.98.11"   # IP address of the RSU (broker for all OBUs)
BROKER_PORT = 1883                # Standard MQTT port

# Topics for communication
TOPIC_ANNOUNCE = "vanetza/announce"
TOPIC_PARKING_STATUS = "vanetza/parking_status"

# Define station IDs and coordinates
RSU_ID = 1
OBU_DETAILS = {
    3: {"lat": 40.7128, "lon": -74.0060},
    4: {"lat": 34.0522, "lon": -118.2437},
    5: {"lat": 37.7749, "lon": -122.4194},
    6: {"lat": 51.5074, "lon": -0.1278},
}

# Create announcement message
def create_announce_message(station_id, station_type, lat, lon):
    return {
        "station_id": station_id,
        "station_type": station_type,
        "message": "Announce presence",
        "latitude": lat,
        "longitude": lon,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# Create parking status message
def create_parking_status_message(station_id, status, lat, lon):
    return {
        "station_id": station_id,
        "status": status,
        "latitude": lat,
        "longitude": lon,
        "timestamp": datetime.now(timezone.utc).isoformat()
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
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    timestamp = data.get("timestamp")

    print(f"Station {station_id} at ({latitude}, {longitude}) reports status: {status} at {timestamp}")

    if status == "parking_request":
        print(f"Station {station_id} requests to park. Granting permission.")
        response = create_parking_status_message(RSU_ID, "parking_granted", latitude, longitude)
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
        for obu_id, coords in OBU_DETAILS.items():
            announce_msg = create_announce_message(obu_id, 5, coords["lat"], coords["lon"])
            client.publish(TOPIC_ANNOUNCE, json.dumps(announce_msg))
            print(f"Announced presence for OBU {obu_id} at ({coords['lat']}, {coords['lon']})")

            parking_request_msg = create_parking_status_message(obu_id, "parking_request", coords["lat"], coords["lon"])
            client.publish(TOPIC_PARKING_STATUS, json.dumps(parking_request_msg))
            print(f"Parking request sent for OBU {obu_id} at ({coords['lat']}, {coords['lon']})")

        time.sleep(10)

except KeyboardInterrupt:
    print("Stopping script.")
    client.loop_stop()
    client.disconnect()
