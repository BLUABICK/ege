from ipaddress import *
def f(ip):
    ip = f'{int(ip):023b}'
    return ip[:16].count('1')>=ip[16:].count('1')
for mask in range(16,25):
    net = ip_network(f'238.51.1.202/{mask}', 0)
    if all(f(i) for i in net):
        print(net.netmask)
        break