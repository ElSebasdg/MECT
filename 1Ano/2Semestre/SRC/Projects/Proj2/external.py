import pandas as pd
import numpy as np
import ipaddress
import pygeoip
from collections import defaultdict
from sklearn.ensemble import IsolationForest

### INITIAL SETUP ------------------------
# Load GeoIP databases

# Define student numbers and calculate X
nmec1 = 103411
nmec2 = 103690
X = (nmec1 + nmec2) % 10
gi = pygeoip.GeoIP('./GeoIP_DBs/GeoIP.dat')
gi2 = pygeoip.GeoIP('./GeoIP_DBs/GeoIPASNum.dat')
# File path for serversX.parquet
serversfile = f'./datasets/dataset{X}/servers{X}.parquet'
# Read the serversX.parquet data file
servers_data = pd.read_parquet(serversfile)

### HELPER FUNCTIONS ------------------------
# Remove duplicates from array
def remove_duplicates_set(arr):
    return list(set(arr))

# Return network object for ip address
def get_network(ip, subnet_mask="255.255.255.0"):
    network = ipaddress.ip_network(f'{ip}/{subnet_mask}', strict=False)
    return network

# Identifies if ip address is in network
def is_ip_in_network(ip, network):
    return ipaddress.ip_address(ip) in network

### ANALYSIS FUNCTION ------------------------
def detect_anomalies_in_external_accesses(servers_data):
    # Define the internal network of the corporation servers
    corporation_network = ipaddress.ip_network('200.0.0.0/24')

    # Filter external accesses to the corporation servers
    external_accesses = servers_data[~servers_data['src_ip'].apply(lambda ip: ipaddress.ip_address(ip) in corporation_network)]

    # Analyze access patterns (you can customize this based on your specific requirements)
    access_patterns = external_accesses.groupby(['src_ip', 'dst_ip']).size().reset_index(name='access_count')

    # Use Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.1)  # Adjust contamination based on expected anomaly rate
    access_patterns['anomaly_score'] = model.fit_predict(access_patterns[['access_count']])

    # Identify potential anomalies
    potential_anomalies = access_patterns[access_patterns['anomaly_score'] == -1]

    return potential_anomalies

### EXECUTE ANALYSIS ------------------------
potential_anomalies = detect_anomalies_in_external_accesses(servers_data)

### PRINT POTENTIAL ANOMALIES ------------------------
print("Potential Anomalies:")
print(potential_anomalies)

# Additional contextual analysis and investigation steps can be added based on your requirements
