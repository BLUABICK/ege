from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')

for A in range(256)[::-1]:
    net = ip_network(f'223.167.{A}.167/26', False)
    if all(f(i) for i in net):
        print(A)
        break
