from ipaddress import *

ip = ip_network('73.148.145.65/255.224.0.0', 0).hosts()
print(str(list(ip)[-1]).replace('.',''))