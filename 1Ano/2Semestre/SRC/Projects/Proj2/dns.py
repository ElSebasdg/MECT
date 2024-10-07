import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pygeoip

# Ajustar o estilo dos gráficos
sns.set(style="whitegrid")

# Define student numbers and calculate X
nmec1 = 103411
nmec2 = 103690
X = (nmec1 + nmec2) % 10

# File paths
datafile = f'./datasets/dataset{X}/data{X}.parquet'
geoip_db_country = './GeoIP_DBs/GeoIP.dat'
geoip_db_asn = './GeoIP_DBs/GeoIPASNum.dat'

# Read parquet data files
data = pd.read_parquet(datafile)

# Filtragem ajustada
dns_traffic_data = data[((data['proto'].str.lower() == 'udp') & (data['port'] == 53)) | 
                        ((data['proto'].str.lower() == 'tcp') & (data['port'] == 443))]

if dns_traffic_data.empty:
    print("No DNS records found. Check the data and filtering.")
else:
    # Initialize GeoIP
    gi_country = pygeoip.GeoIP(geoip_db_country)
    gi_asn = pygeoip.GeoIP(geoip_db_asn)
    
    # Function to get country of an IP
    def get_country(ip):
        try:
            return gi_country.country_name_by_addr(ip) or 'Unknown'
        except Exception:
            return 'Unknown'
    
    # Function to get ASN of an IP
    def get_asn(ip):
        try:
            return gi_asn.org_by_addr(ip) or 'Unknown'
        except Exception:
            return 'Unknown'
    
    # Add country and ASN information
    dns_traffic_data['src_country'] = dns_traffic_data['src_ip'].apply(get_country)
    dns_traffic_data['dst_country'] = dns_traffic_data['dst_ip'].apply(get_country)
    dns_traffic_data['src_asn'] = dns_traffic_data['src_ip'].apply(get_asn)
    dns_traffic_data['dst_asn'] = dns_traffic_data['dst_ip'].apply(get_asn)

    # Function to save adjusted figures
    def save_fig_adjusted(filename, dpi=300):
        plt.savefig(filename, bbox_inches='tight', dpi=dpi)
        plt.close()

    # Count the number of queries per destination IP
    dst_ip_counts = dns_traffic_data['dst_ip'].value_counts()
    
    # Statistical analysis to find outliers
    mean_count = dst_ip_counts.mean()
    std_count = dst_ip_counts.std()
    threshold = mean_count + 3 * std_count  # Define a threshold as mean + 3 * standard deviation
    
    # Detect suspicious IPs
    suspicious_ips = dst_ip_counts[dst_ip_counts > threshold].index.tolist()
    suspicious_counts = dst_ip_counts[dst_ip_counts > threshold]

    if suspicious_ips:
        print("Suspicious IPs detected:")
        for ip, count in suspicious_counts.items():
            print(f"IP: {ip}, Queries: {count}")
    else:
        print("No suspicious IPs detected.")

    # Visualize the suspicious IPs
    plt.figure(figsize=(12, 8))
    sns.barplot(x=suspicious_counts.values, y=suspicious_counts.index, palette='magma')
    plt.title("Suspicious Destination IPs with Significantly More Queries", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("Destination IP", fontsize=14)
    save_fig_adjusted('suspicious_dst_ips.png')
