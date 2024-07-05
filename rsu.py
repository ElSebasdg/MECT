import json
import datetime
import threading
import paho.mqtt.client as mqtt

RSU_BROKER_IP = "192.168.98.11"  # IP address of the MQTT broker
BROKER_PORT = 1883
MQTT_TOPICS = ["obu/to/rsu"]

obu_locations = {}

# Define available parking locations
AVAILABLE_PARKING = [
    {"name": "Parking Lot A", "latitude": 40.630321, "longitude": -8.657457},
    {"name": "Parking Lot B", "latitude": 40.629555, "longitude": -8.656427}
]

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with code {rc}")
    for topic in MQTT_TOPICS:
        client.subscribe(topic)
    
    # Check if no OBUs are parked initially
    if not obu_locations:
        notify_available_parking(client)

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload)
        print(f"RSU Received message on {msg.topic}: {message}")

        if msg.topic == "obu/to/rsu":
            obu_id = message['obu_id']
            location = message['location']
            obu_locations[obu_id] = location  # Update or add the location of the OBU

            print("--------------------------------------------------------------------------")
            print(obu_locations)

            
            # Respond with acknowledgment if needed
            response = {
                "response": f"RSU Acknowledges the message from OBU {obu_id}",
                "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
            }
            client.publish("rsu/to/obu", json.dumps(response))
            print(f"RSU sent response: {response}")

    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload}")

def notify_available_parking(client):
    # Construct message with available parking locations
    message = {
        "available_parking": AVAILABLE_PARKING,
        "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
    }
    client.publish("rsu/to/obu", json.dumps(message))
    print(f"RSU sent available parking information: {message}")

def get_obu_location(obu_id):
    return obu_locations.get(obu_id)

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(RSU_BROKER_IP, BROKER_PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    threading.Thread(target=start_mqtt_client).start()
