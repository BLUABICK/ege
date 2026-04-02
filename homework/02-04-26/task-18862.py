from ipaddress import *

net = ip_network('172.140.68.0/255.255.248.0', 0)
cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('0')>15:
        cnt+=1
print(cnt)