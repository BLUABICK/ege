from ipaddress import *

ip = ip_network(r'172.95.116.174/255.255.192.0', 0)

for i in ip:
    print(i)

print(eval('172.95.64.1'.replace('.', '+')))