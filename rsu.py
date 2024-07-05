import json
import datetime
import paho.mqtt.client as mqtt

BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("obu/to/rsu")  # Subscribe to messages from OBU

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload)
        print(f"RSU Received message on {msg.topic}: {message}")

        if msg.topic == "obu/to/rsu":
            obu_id = message['obu_id']
            response = {
                "response": f"RSU Acknowledges the message from OBU {obu_id}",
                "timestamp": datetime.datetime.utcnow().isoformat() + 'Z'
            }
            client.publish("rsu/to/obu", json.dumps(response))
            print(f"RSU sent response: {response}")

    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload}")

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_IP, BROKER_PORT, 60)
    client.loop_forever()
