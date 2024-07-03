import time
import random
from vanetza.client import Client
from vanetza.datex import CooperativeAwarenessMessage

# Configuration
RSU_IP = '192.168.98.11'  # Replace with your RSU's IP
RSU_PORT = 1789  # Default port for Vanetza CAM messages

# Initialize Vanetza client
client = Client()
client.connect(RSU_IP, RSU_PORT)

# Simulate OBU behavior
while True:
    # Generate random OBU data
    station_id = random.randint(1, 6)
    latitude = random.uniform(40.63, 40.66)  # Adjust coordinates based on your campus
    longitude = random.uniform(-8.65, -8.61)  # Adjust coordinates based on your campus
    
    # Create CAM message
    cam = CooperativeAwarenessMessage(
        station_id=station_id,
        latitude=latitude,
        longitude=longitude,
        heading=0,  # Example heading
        speed=0,  # Example speed
    )
    
    # Send CAM message to RSU
    client.send(cam)
    
    # Print simulation info
    print(f"Sent CAM message from OBU {station_id} at ({latitude}, {longitude})")
    
    # Wait for next iteration
    time.sleep(5)  # Adjust timing as needed
