from ipaddress import *

net = ip_network('98.81.154.195/255.252.0.0', 0)
maxxi=0
for i in net:
    i= f'{int(i):032b}'
    if int(i)>maxxi:
        maxxi = int(i)
print(maxxi)
print(int('11000100',2),int('10100111',2),int('11111111',2),int('11111111',2))