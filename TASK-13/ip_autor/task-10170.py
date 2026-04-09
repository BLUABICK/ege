from ipaddress import *

ip_1 = ip_address('193.175.175.231')
ip_2 = ip_address('193.175.176.118')

for mask in range(16, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net and ip_2 not in net:
        print(str(net.netmask)[8:11])
        break