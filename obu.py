import time
import json
import datetime
import threading
import paho.mqtt.client as mqtt

BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

OBUs = [
    {
        
        'id': 1,
        # 'animation_path': [
        #     [40.630321, -8.657457]
        # ]
        'animation_path': [
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
            [40.6314, -8.6578]
        ]
    },
    {
        'id': 2,
        'animation_path': [
            #[40.630321, -8.657457]
            [40.629555, -8.656427]
        ]
        # 'animation_path': [
        #     [40.6314, -8.6578],
        #     [40.6312, -8.6581],
        #     [40.6308, -8.6585],
        #     [40.6305, -8.6587],
        #     [40.6301, -8.6592],
        #     [40.6298, -8.6588],
        #     [40.6294, -8.6582],
        #     [40.6289, -8.6576],
        #     [40.6285, -8.6561],
        #     [40.6292, -8.6550],
        #     [40.6305, -8.6554],
        #     [40.6312, -8.6563],
        #     [40.6312, -8.6564]
        # ]
    }
]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe("rsu/to/obu")  # Subscribe to receive acknowledgments from RSU
    else:
        print(f"Failed to connect, return code: {rc}")

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload)
        print(f"OBU Received message on {msg.topic}: {message}")
        
        # Check if the message is an acknowledgment from RSU
        if msg.topic == "rsu/to/obu":
            handle_acknowledgment(message)

    except json.JSONDecodeError:
        print(f"Received non-JSON message on {msg.topic}: {msg.payload}")

def handle_acknowledgment(message):
    # Example logic to handle acknowledgment received from RSU
    print(f"OBU received acknowledgment from RSU: {message}")

def simulate_obu_movements(client, obu_data):
    obu_id = obu_data['id']
    animation_path = obu_data['animation_path']
    
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
        
        # Publish message to vanetza/parking_status topic
        client.publish("vanetza/parking_status", json.dumps(message))
        print(f"OBU {obu_id} sent message: {message}")
        
        # Publish message to obu/to/rsu topic
        rsu_message = {
            "obu_id": obu_id,
            "message": "OBU at new location",
            "location": {"lat": lat, "lon": lon},
            "timestamp": timestamp
        }
        client.publish("obu/to/rsu", json.dumps(rsu_message))
        
        idx = (idx + 1) % len(animation_path)
        time.sleep(2)  # Adjust the sleep time for desired speed

def start_obu_simulations(client):
    threads = []
    for obu in OBUs:
        thread = threading.Thread(target=simulate_obu_movements, args=(client, obu))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_IP, BROKER_PORT, 60)
    client.loop_start()
    
    start_obu_simulations(client)
