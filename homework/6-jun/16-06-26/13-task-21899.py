from ipaddress import *

ip = ip_network('98.81.154.195/255.252.0.0', 0).hosts()
print(str(max(*ip)).replace('.', ''))