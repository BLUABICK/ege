from ipaddress import *

net = ip_network('214.96.0.0/255.240.0.0')
cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('0')%3==0:
        cnt+=1
print(cnt)