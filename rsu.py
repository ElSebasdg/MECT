import json
import paho.mqtt.client as mqtt
import datetime

BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("obu/to/rsu")  # Subscribe to messages from OBU

# Callback for when a message is received
def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload)
        print(f"RSU Received message on {msg.topic}: {message}")

        if msg.topic == "obu/to/rsu":
            response = {
                "response": "RSU Acknowledges the message",
                "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
            }
            client.publish("rsu/to/obu", json.dumps(response))
            print(f"RSU sent response: {response}")

    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload}")

# Initialize the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(BROKER_IP, BROKER_PORT, 60)
client.loop_forever()
