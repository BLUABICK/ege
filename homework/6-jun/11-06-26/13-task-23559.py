from ipaddress import *

ip = list(ip_network('102.162.200.51/255.255.255.0', 0).hosts())

print(eval(str(ip[-1]).replace('.','+')))
