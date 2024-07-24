# pip install pygeoip
# pip install fastparquet 
# pip install dnspython
import pandas as pd
import numpy as np
import ipaddress
import dns.resolver
import dns.reversename
import pygeoip
import matplotlib.pyplot as plt 

nmecMauro = 103411
nmecSebastian = 103690
num = (nmecMauro + nmecSebastian)%10
datafile='./datasets/dataset'+str(num)+'/data'+str(num)+'.parquet'

### IP geolocalization
gi=pygeoip.GeoIP('./GeoIP_DBs/GeoIP.dat')
gi2=pygeoip.GeoIP('./GeoIP_DBs/GeoIPASNum.dat')
addr='193.136.73.21'
cc=gi.country_code_by_addr(addr)
org=gi2.org_by_addr(addr)
print(cc,org)

### DNS resolution
addr=dns.resolver.resolve("www.ua.pt", 'A')
for a in addr:
    print(a)
    
### Reverse DNS resolution    
name=dns.reversename.from_address("193.136.172.20")
addr=dns.resolver.resolve(name, 'PTR')
for a in addr:
    print(a)

### Read parquet data files
data=pd.read_parquet(datafile)
#print(data.to_string())

#Just the UDP flows
udpF=data.loc[data['proto']=='udp']

#Number of UDP flows for each source IP
nudpF=data.loc[data['proto']=='udp'].groupby(['src_ip'])['up_bytes'].count()

#Number of UDP flows to port 443, for each source IP
nudpF443=data.loc[(data['proto']=='udp')&(data['port']==443)].groupby(['src_ip'])['up_bytes'].count()

#Average number of downloaded bytes, per flow, for each source IP
avgUp=data.groupby(['src_ip'])['down_bytes'].mean()


#Total uploaded bytes to destination port 443, for each source IP, ordered from larger amount to lowest amount
upS=data.loc[((data['port']==443))].groupby(['src_ip'])['up_bytes'].sum().sort_values(ascending=False)

#Histogram of the total uploaded bytes to destination port 443, by source IP
upS=data.loc[((data['port']==443))].groupby(['src_ip'])['up_bytes'].sum().hist()
#plt.show()

#Upload/Download bytes ratio (traffic for port 443) for each source IP
a1=data.loc[((data['port']==443))].groupby(['src_ip'])['up_bytes'].sum()
a2=data.loc[((data['port']==443))].groupby(['src_ip'])['down_bytes'].sum()
a3=pd.DataFrame(a2/a1,columns=['ratio'])

#Is destination IPv4 a public address?
NET=ipaddress.IPv4Network('192.168.100.0/24')
bpublic=data.apply(lambda x: ipaddress.IPv4Address(x['dst_ip']) not in NET,axis=1)

#Geolocalization of public destination adddress
cc=data[bpublic]['dst_ip'].apply(lambda y:gi.country_code_by_addr(y)).to_frame(name='cc')

#Average interval between flows from same source IP (for each source IP)
data['diff_timestamp']=data.groupby(['src_ip'])['timestamp'].diff().fillna(0)
data.groupby(['src_ip'])['diff_timestamp'].mean().sort_values(ascending=False)
