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
testfile = f'./datasets/dataset{X}/test{X}.parquet'
serversfile = f'./datasets/dataset{X}/servers{X}.parquet'
geoip_db_country = './GeoIP_DBs/GeoIP.dat'
geoip_db_asn = './GeoIP_DBs/GeoIPASNum.dat'

# Read parquet data files
data = pd.read_parquet(datafile)
test_data = pd.read_parquet(testfile)
servers_data = pd.read_parquet(serversfile)

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

    # Top 10 DNS Server Countries
    dns_servers_country = dns_traffic_data['dst_country'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=dns_servers_country.values, y=dns_servers_country.index, palette='viridis')
    plt.title("Top 10 DNS Server Countries", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("Country", fontsize=14)
    save_fig_adjusted('top_dns_servers_country.png')

    # Top 10 Source IP Countries
    src_country_counts = dns_traffic_data['src_country'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=src_country_counts.values, y=src_country_counts.index, palette='coolwarm')
    plt.title("Top 10 Source IP Countries", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("Country", fontsize=14)
    save_fig_adjusted('top_src_ips_country.png')

    # Top 10 Source IP ASNs
    src_asn_counts = dns_traffic_data['src_asn'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=src_asn_counts.values, y=src_asn_counts.index, palette='coolwarm')
    plt.title("Top 10 Source IP ASNs", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("ASN", fontsize=14)
    save_fig_adjusted('top_src_asn.png')

    # Top 10 Destination IP ASNs
    dst_asn_counts = dns_traffic_data['dst_asn'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=dst_asn_counts.values, y=dst_asn_counts.index, palette='magma')
    plt.title("Top 10 Destination IP ASNs", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("ASN", fontsize=14)
    save_fig_adjusted('top_dst_asn.png')

    # Top 10 Source IPs with Most Queries
    src_counts = dns_traffic_data['src_ip'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=src_counts.values, y=src_counts.index, palette='coolwarm')
    plt.title("Top 10 Source IPs with Most Queries", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("Source IP", fontsize=14)
    save_fig_adjusted('top_src_ips.png')

    # Top 10 Destination IPs with Most Queries
    dst_counts = dns_traffic_data['dst_ip'].value_counts().head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=dst_counts.values, y=dst_counts.index, palette='magma')
    plt.title("Top 10 Destination IPs with Most Queries", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("Destination IP", fontsize=14)
    save_fig_adjusted('top_dst_ips.png')

    # Top 10 IP Pairs (Source -> Destination) with Most DNS Queries
    src_to_dst_counts = dns_traffic_data.groupby(['src_ip', 'dst_ip']).size().nlargest(10)
    src_to_dst_df = src_to_dst_counts.reset_index(name='count')
    plt.figure(figsize=(14, 8))
    sns.barplot(x='count', y=src_to_dst_df.apply(lambda x: f"{x['src_ip']} -> {x['dst_ip']}", axis=1), data=src_to_dst_df, palette='plasma')
    plt.title("Top 10 IP Pairs (Source -> Destination) with Most DNS Queries", fontsize=16)
    plt.xlabel("Number of Queries", fontsize=14)
    plt.ylabel("IP Pairs (Source -> Destination)", fontsize=14)
    save_fig_adjusted('top_ip_pairs.png')

    # Top 10 Source IPs Querying Many DNS Servers
    src_to_many_dsts = dns_traffic_data.groupby('src_ip')['dst_ip'].nunique().nlargest(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=src_to_many_dsts.values, y=src_to_many_dsts.index, palette='inferno')
    plt.title("Top 10 Source IPs Querying Many DNS Servers", fontsize=16)
    plt.xlabel("Number of Queried DNS Servers", fontsize=14)
    plt.ylabel("Source IP", fontsize=14)
    save_fig_adjusted('top_src_many_dst.png')

# Analyze access outside business hours
def analyze_public_service_access(access_data):
    access_data['timestamp'] = pd.to_datetime(access_data['timestamp'])
    access_data['hour'] = access_data['timestamp'].dt.hour
    
    out_of_hours = access_data[(access_data['hour'] < 8) | (access_data['hour'] > 18)]
    ip_counts = out_of_hours['src_ip'].value_counts().head(20)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x=ip_counts.values, y=ip_counts.index, palette='dark')
    plt.title("Top IPs with Unusual Access Outside Business Hours", fontsize=16)
    plt.xlabel("Number of Accesses Outside Business Hours", fontsize=14)
    plt.ylabel("Source IP", fontsize=14)
    save_fig_adjusted('top_out_of_hours_access.png')
    
    return ip_counts

# Run access analysis
anomalous_ips = analyze_public_service_access(servers_data)
