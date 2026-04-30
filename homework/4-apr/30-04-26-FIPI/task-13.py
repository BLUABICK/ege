from ipaddress import *
ip_1 = ip_address('68.203.243.87')
ip = ip_network(r'68.203.243.87/255.255.224.0', 0)

if ip_1 in ip:
    print(eval(str(list(ip.hosts())[-1]).replace('.', '+')))