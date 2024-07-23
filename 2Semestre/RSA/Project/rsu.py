import json
import datetime
import threading
import paho.mqtt.client as mqtt

RSU_BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883
MQTT_TOPICS = ["obu/to/rsu"]

obu_locations = {}

# Define available parking locations
AVAILABLE_PARKING = [
    {"name": "ParkingLot1", "latitude": 40.630321, "longitude": -8.657457},
    {"name": "ParkingLot2", "latitude": 40.629555, "longitude": -8.656427}
]

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with code {rc}")
    for topic in MQTT_TOPICS:
        client.subscribe(topic)
    
    if not obu_locations:
        notify_available_parking(client)

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload)
        print(f"RSU Received message on {msg.topic}: {message}")

        if msg.topic == "obu/to/rsu":
            obu_id = message['obu_id']
            location = message['location']
            obu_locations[obu_id] = location

            print("\n---------------------------------------")
            print("obu_locations:", obu_locations)
            print("AVAILABLE_PARKING:", AVAILABLE_PARKING)
            print("---------------------------------------\n")


            response = {
                "response": f"RSU Acknowledges the message from OBU {obu_id}",
                "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
            }
            client.publish("rsu/to/obu", json.dumps(response))
            print(f"RSU sent response: {response}")

            notify_available_parking(client)  # Update parking status

    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload}")

def check_parking_status():
    parking_status = {}
    for parking in AVAILABLE_PARKING:
        is_occupied = any(
            abs(obu['lat'] - parking['latitude']) < 1e-6 and abs(obu['lon'] - parking['longitude']) < 1e-6
            for obu in obu_locations.values()
        )
        parking_status[parking['name']] = not is_occupied  # True if available, False if occupied
    return parking_status

def notify_available_parking(client):
    parking_status = check_parking_status()
    message = {
        "available_parking": AVAILABLE_PARKING,
        "parking_status": parking_status,
        "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
    }
    client.publish("rsu/to/obu", json.dumps(message))
    print(f"RSU sent available parking information: {message}")

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(RSU_BROKER_IP, BROKER_PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    threading.Thread(target=start_mqtt_client).start()
