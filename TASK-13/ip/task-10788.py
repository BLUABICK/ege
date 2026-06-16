from ipaddress import *
ip_1 = ip_address('201.44.240.33')
ip_2 = ip_address('201.44.240.107')
cnt = 0
for x in range(10, 31):
    net_1 = ip_network(f'{ip_1}/{x}', 0)
    if ip_1 in net_1.hosts() and ip_2 in net_1.hosts():
        ne = f'{int(net_1[0]):032b}'
        if ne.count('1')>=5:
            cnt+=1
print(cnt)