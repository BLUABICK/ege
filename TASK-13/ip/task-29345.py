from ipaddress import ip_network


net = ip_network('68.203.243.87/255.255.224.0', 0)

print(eval(str(net[-2]).replace('.', '+')))