# Библиотека для работы с ip_адресами
from ipaddress import *

# Конвертирует текст в объект ip_address
ip = ip_address('192.0.0.5')

# Формирует все ip_адреса по заданной сети и маске
net = ip_network('192.0.0.5/255.255.255.0', 0)
net = ip_network('192.0.0.5/29', 0)

# Широковещательный адрес. Не может быть присвоен устройству
broadcast_address = net.broadcast_address

# Адрес сети. Не может быть присвоен устройству
network_address = net.network_address

# Хосты - ip_адреса, которые могут быть присвоены устройством
hosts = net.hosts()

# Двоичное представление ip_адреса с добавлением ведущих нулей до 32х позиций
bin_ip = f'{int(broadcast_address):032b}'