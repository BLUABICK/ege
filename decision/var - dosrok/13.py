from ipaddress import *

net = ip_network('146.180.173.153/255.192.0.0', 0)
max_i = 1
for i in net:
    i = int(f'{int(i):032b}')
    if max_i<i:
        max_i = i
print(sum([int(str(max_i)[:8], 2),int(str(max_i)[8:16], 2),int(str(max_i)[16:24], 2),int(str(max_i)[24:32],2 )])-1)