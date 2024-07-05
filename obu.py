import time
import json
import datetime
import threading
import paho.mqtt.client as mqtt

BROKER_IP = "192.168.98.11"
BROKER_PORT = 1883

# Define the parking route
PARKING_ROUTE = [
    [40.630581, -8.657892],
    [40.630976, -8.657382],
    [40.630748, -8.656846],
    [40.630545, -8.656363],
    [40.630239, -8.656765]
]

# Define the OBUs with their respective paths
OBUs = [
    {
        'id': 1,
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
            [40.629555, -8.656427]  # Initial location near parking lot 2
        ]
    }
]


AVAILABLE_PARKING = [
    [40.630321, -8.657457],
    [40.629555, -8.656427]
]

# Callback function when the OBU connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe("rsu/to/obu")  # Subscribe to receive acknowledgments from RSU
    else:
        print(f"Failed to connect, return code: {rc}")

# Callback function when a message is received
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
    print(f"OBU received acknowledgment from RSU: {message}")
    parking_status = message.get("parking_status", {})
    available_parking = message.get("available_parking", [])
    print("EHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n")
    print("AVAILABLE: ", available_parking )
    # Select an available parking lot if any
    chosen_parking = None
    for parking in available_parking:
        if parking_status.get(parking["name"], True):  # Look for the first not occupied parking

            chosen_parking = parking
            print("\nAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n")
            print("chosen_parking: ", chosen_parking )
            break

    # Update OBU routes based on parking availability
    for obu in OBUs:
        idx = obu.get('current_idx', 0)
        if idx == 12:
            if chosen_parking:
                # Extend the route with the parking lot coordinates
                extended_parking_route = PARKING_ROUTE + [[chosen_parking["latitude"], chosen_parking["longitude"]]]
                obu['animation_path'] = extended_parking_route
                print(f"OBU {obu['id']} is directing to {chosen_parking['name']} at location ({chosen_parking['latitude']}, {chosen_parking['longitude']})")
            else:
                print(f"OBU {obu['id']} continues on its default route.")

def simulate_obu_movements(client, obu_data):
    obu_id = obu_data['id']
    idx = 0

    while True:
        obu_data['current_idx'] = idx  # Track current index
        animation_path = obu_data['animation_path']  # Fetch the latest path
        lat, lon = animation_path[idx]
        

        print(f"\nOBU {obu_id} is currently at: Latitude {lat}, Longitude {lon}\n")  # Print current position
        

        timestamp = datetime.datetime.utcnow().isoformat() + 'Z'
        message = {
            "station_id": obu_id,
            "status": "moving",
            "latitude": lat,
            "longitude": lon,
            "timestamp": timestamp
        }
        
        # Publish to vanetza/parking_status topic
        client.publish("vanetza/parking_status", json.dumps(message))
        print(f"OBU {obu_id} sent message: {message}")
        
        # Publish to obu/to/rsu topic
        rsu_message = {
            "obu_id": obu_id,
            "message": "OBU at new location",
            "location": {"lat": lat, "lon": lon},
            "timestamp": timestamp
        }
        client.publish("obu/to/rsu", json.dumps(rsu_message))
        
        # Check if the OBU has reached index 12 and update its route if necessary
        if idx == 12:
            if 'chosen_parking' in obu_data:
                print(f"OBU {obu_id} is parking at chosen parking lot.")
            else:
                print(f"OBU {obu_id} continues to its next destination.")
        

        print(f"\nOBU {obu_id} is currently at: Latitude {lat}, Longitude {lon}\n")  # Print current position
        print("\n idx: ", idx, "\n")

        for parking in AVAILABLE_PARKING:
            if abs(lat - parking[0]) < 1e-6 and abs(lon - parking[1]) < 1e-6:
                obu_data['animation_path'] = [parking]  # Set animation_path to the parking location

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
