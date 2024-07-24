import pandas as pd
import numpy as np
import ipaddress
import pygeoip
import matplotlib.pyplot as plt
from collections import defaultdict



### INITIAL SETUP ------------------------
# Define student numbers and calculate X
nmec1 = 103411
nmec2 = 103690
X = (nmec1 + nmec2) % 10
# File paths
datafile = f'./datasets/dataset{X}/data{X}.parquet'
testfile = f'./datasets/dataset{X}/test{X}.parquet'
serversfile = f'./datasets/dataset{X}/servers{X}.parquet'
# Load GeoIP databases
gi = pygeoip.GeoIP('./GeoIP_DBs/GeoIP.dat')
gi2 = pygeoip.GeoIP('./GeoIP_DBs/GeoIPASNum.dat')
# Read parquet data files
data = pd.read_parquet(datafile)
test_data = pd.read_parquet(testfile)
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



### ANALYSIS FUNCTIONS ------------------------
def nonAnomalousAnalysisData(dataFrame):
    # Descriptive stats
    print("\nStats: ")
    print(dataFrame.describe())
    # Traffic volume over time
    traffic_time = dataFrame.groupby(pd.Grouper(key='timestamp')).size()
    plt.figure(figsize=(14, 7))
    plt.plot(traffic_time.index, traffic_time.values, label='traffic')
    plt.xlabel('Time')
    plt.ylabel('Number of Packets')
    plt.title('Traffic Volume Over Time')
    plt.legend()
    plt.show()
    # Traffic distribution by destination IP
    traffic_distribution = dataFrame['dst_ip'].value_counts()
    print("\nTraffic - destination count:\n", traffic_distribution)
    plt.figure(figsize=(12, 6))
    traffic_distribution.head(15).plot(kind='bar')
    plt.xlabel('Destination IP')
    plt.ylabel('Frequency')
    plt.title('Traffic - destination count')
    plt.show()
    # Distribution by country
    traffic_countries = dataFrame['country'].value_counts()
    print("\nTraffic - destination country:\n", traffic_countries)
    # Distribution by protocols
    traffic_protocols = dataFrame["proto"].value_counts()
    print("\nTraffic - protocols:\n", traffic_protocols)
    # Distribution by port
    traffic_port = dataFrame["port"].value_counts()
    print("\nTraffic - port:\n", traffic_port)

def topUploadersAnalysis(normalDataFrame):
    normal_up_bytes = normalDataFrame.groupby('src_ip')['up_bytes'].mean()
    top_uploaders = normal_up_bytes.sort_values(ascending=False).head(10)
    org_uploads = {}
    country_uploads = {}
    for ip in top_uploaders.index:
        avg_bytes = top_uploaders[ip]
        print(f"IP: {ip}, Average Upload Bytes: {avg_bytes}")
    print("\n")
    for ip in top_uploaders.index:
        ip_data = normalDataFrame[normalDataFrame['src_ip'] == ip]
        dst_ip_bytes = ip_data.groupby('dst_ip')['up_bytes'].sum().sort_values(ascending=False)
        orgs = dst_ip_bytes.index.map(lambda x: gi2.org_by_addr(x))
        countries = dst_ip_bytes.index.map(lambda x: gi.country_code_by_addr(x))
        for org, bytes_received in zip(orgs, dst_ip_bytes):
            if org in org_uploads:
                org_uploads[org] += bytes_received
            else:
                org_uploads[org] = bytes_received
        for country, bytes_received in zip(countries, dst_ip_bytes):
            if country in country_uploads:
                country_uploads[country] += bytes_received
            else:
                country_uploads[country] = bytes_received
    top_orgs = sorted(org_uploads.items(), key=lambda x: x[1], reverse=True)[:10]
    top_countries = sorted(country_uploads.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 Organizations Receiving Uploads:")
    for org, bytes_received in top_orgs:
        print(f"Organization: {org}, Total Bytes: {bytes_received}")
    print("\nTop 10 Countries Receiving Uploads:")
    for country, bytes_received in top_countries:
        print(f"Country: {country}, Total Bytes: {bytes_received}")

def internalBotNetAnalysis(dataFrameData, dataFrameTest):
    # Gets all dst ips for each src ip in normal data
    normal_src_to_dst_dict = {}
    for src_ip in dataFrameData['src_ip'].unique():
        src_data = dataFrameData[dataFrameData['src_ip'] == src_ip]
        top_dst_ips = src_data['dst_ip'].value_counts().index.tolist()
        normal_src_to_dst_dict[src_ip] = top_dst_ips
    # Gets all dst ips for each src ip in test data
    test_src_to_dst_dict = {}
    for src_ip in dataFrameTest['src_ip'].unique():
        src_data = dataFrameTest[dataFrameTest['src_ip'] == src_ip]
        top_dst_ips = src_data['dst_ip'].value_counts().index.tolist()
        test_src_to_dst_dict[src_ip] = top_dst_ips
    # Gets, for each new src ip or src ip that communicates with new dst ips, the dst ips that dont match
    # the normal data dst ips
    suspicious_ips = {}
    for src_ip in test_src_to_dst_dict:
        if src_ip not in normal_src_to_dst_dict:
            suspicious_ips[src_ip] = test_src_to_dst_dict[src_ip]
            print(f"Source IP {src_ip} not found in normal data.")
        else:
            normal_dst_ips = set(normal_src_to_dst_dict[src_ip])
            test_dst_ips = set(test_src_to_dst_dict[src_ip])
            if normal_dst_ips != test_dst_ips:
                different_ips = test_dst_ips - normal_dst_ips
                if different_ips:
                    print(f"Source IP {src_ip} has mismatched destination IPs: {different_ips}")
                suspicious_ips[src_ip] = different_ips
    print("\nSUSPICIOIUS IPS:")
    print(suspicious_ips)
    # Filter suspicious IPs based on mutual communication
    filtered_suspicious_ips = {}
    for src_ip, dst_ips in suspicious_ips.items():
        for dst_ip in dst_ips:
            if dst_ip in suspicious_ips and src_ip in suspicious_ips[dst_ip]:
                if src_ip not in filtered_suspicious_ips:
                    filtered_suspicious_ips[src_ip] = []
                filtered_suspicious_ips[src_ip].append(dst_ip)
    suspicious_ips = filtered_suspicious_ips
    print("\nSUSPICIOUS IPS THAT COMMUNICATE WITH OTHER SUSPICIOUS INTERNAL IPS:")
    print(suspicious_ips)
    for sender_ip, receiver_ips in suspicious_ips.items():
        plt.figure(figsize=(10, 5))
        plt.title(f"Communication Timeline - Suspicious Sender IP: {sender_ip}")
        plt.xlabel("Time")
        plt.ylabel("Number of Messages")
        for receiver_ip in receiver_ips:
            sender_data = dataFrameTest[dataFrameTest['src_ip'] == sender_ip]
            receiver_data = sender_data[sender_data['dst_ip'] == receiver_ip]
            plt.plot(receiver_data['timestamp'], range(len(receiver_data)), label=f"Receiver IP: {receiver_ip}")
        plt.legend()
        plt.show()


def dataExfiltrationAnalysis(normalDataFrame, testDataFrame):
    normal_up_bytes = normalDataFrame.groupby('src_ip')['up_bytes'].mean()
    test_up_bytes = testDataFrame.groupby('src_ip')['up_bytes'].mean()
    increases = []
    for ip in test_up_bytes.index:
        normal_bytes = normal_up_bytes.get(ip, 0)
        test_bytes = test_up_bytes[ip]
        increase_percentage = ((test_bytes - normal_bytes) / normal_bytes * 100) if normal_bytes > 0 else float('inf')
        if increase_percentage >= 100:
            increases.append((ip, normal_bytes, test_bytes, increase_percentage))
    increases.sort(key=lambda x: x[3], reverse=True)
    IpsByOrgBySrcIp = {}
    for ip, normal_bytes, test_bytes, increase_percentage in increases:
        print(f"IP: {ip}, Normal: {normal_bytes}, Test: {test_bytes}, Increase: {increase_percentage:.2f}%")
        ip_data = testDataFrame[testDataFrame['src_ip'] == ip]
        dst_ip_bytes = ip_data.groupby('dst_ip')['up_bytes'].sum().sort_values(ascending=False)
        # Orgs receiving the most bits
        orgs = dst_ip_bytes.index.map(lambda x: gi2.org_by_addr(x))
        org_bytes = dst_ip_bytes.groupby(orgs).sum().sort_values(ascending=False)
        # IPs by org
        org_dst_map = {}
        for org, dst_ip in zip(orgs, dst_ip_bytes.index):
            if org not in org_dst_map:
                org_dst_map[org] = {}
            org_dst_map[org][dst_ip] = ip_data[ip_data['dst_ip'] == dst_ip]['up_bytes'].sum()
        finalOrgMap = {}
        for org, bytes_received in org_bytes.head(3).items():
            if bytes_received > 0:
                finalOrgMap[org] = org_dst_map[org]
        IpsByOrgBySrcIp[ip] = finalOrgMap
    print("\n")
    for srcIp, orgDic in IpsByOrgBySrcIp.items():
        total_uploaded_bytes = testDataFrame[testDataFrame['src_ip'] == srcIp]['up_bytes'].sum()
        if total_uploaded_bytes > 500 * 1000000:  # Check if total uploaded bytes exceed 500 MB
            print("Src IP: " + srcIp + " Total upload: " + str(total_uploaded_bytes))
            for org, ipDict in orgDic.items():
                print("    Org: " + org)
                for dstIp, dstBytes in ipDict.items():
                    print("        Dst IP: " + dstIp + ", Total bytes: " + str(dstBytes))
        




"""### ADD FIELDS TO DATA ------------------------
data['country'] = data['dst_ip'].apply(lambda x: gi.country_code_by_addr(x))
servers_data["country"] = servers_data['src_ip'].apply(lambda x: gi.country_code_by_addr(x))"""



### NON-ANOMALOUS BEHAVIOR ------------------------
print("------------ NON-ANOMALOUS BEHAVIOR ------------")
# Identify internal servers/services
data_srcIPs = data['src_ip'].unique()
data_dstIPs = data['dst_ip'].unique()
internalNetwork = get_network(data_srcIPs[0])
internalServers = []
externalServers = []
for ip in data_dstIPs:
    isInternal = is_ip_in_network(ip, internalNetwork)
    if isInternal:
        internalServers.append(ip)
    else:
        externalServers.append(ip)
internalServers = remove_duplicates_set(internalServers)
externalServers = remove_duplicates_set(externalServers)
print("Internal servers: " + str(internalServers))

### Quantify traffic exchanges
traffic_fromInternal = data[data['src_ip'].apply(lambda ip: is_ip_in_network(ip, internalNetwork))]
traffic_fromInternalToInternal = traffic_fromInternal[traffic_fromInternal['dst_ip'].apply(lambda ip: is_ip_in_network(ip, internalNetwork))]
traffic_fromInternalToExternal = traffic_fromInternal[~traffic_fromInternal['dst_ip'].apply(lambda ip: is_ip_in_network(ip, internalNetwork))]

"""## 1- from internal to internal
print("------------ FROM INTERNAL TO INTERNAL ANALYSIS ------------")
nonAnomalousAnalysisData(traffic_fromInternalToInternal)
## 2- from internal to external
print("------------ FROM INTERNAL TO EXTERNAL ANALYSIS ------------")
nonAnomalousAnalysisData(traffic_fromInternalToExternal)
topUploadersAnalysis(traffic_fromInternalToExternal)
## 3- from external to public server
print("------------ FROM EXTERNAL TO PUBLIC SERVERS ------------")
server_clientIPs = servers_data['src_ip'].unique()
server_serverIPs = servers_data['dst_ip'].unique()
print("Public servers: " + str(server_serverIPs))
nonAnomalousAnalysisData(servers_data)"""

### SIEM Rules ------------------------
## BotNet 
# - Suspicious communication between internal and internal (which dont usually interact)
trafficTest_fromInternalToInternal = test_data[test_data['dst_ip'].apply(lambda ip: is_ip_in_network(ip, internalNetwork))]
internalBotNetAnalysis(traffic_fromInternalToInternal, trafficTest_fromInternalToInternal)

## Data Exfiltration Using HTTPS or DNS
# - Transfer large volumes of data from internal to external
trafficTest_fromInternalToExternal = test_data[~test_data['dst_ip'].apply(lambda ip: is_ip_in_network(ip, internalNetwork))]
dataExfiltrationAnalysis(traffic_fromInternalToExternal, trafficTest_fromInternalToExternal)