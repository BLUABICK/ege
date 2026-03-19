from math import *

with open(r'..\files\17_3749.txt') as file:
    data = [int(i) for i in file]

sqrt_max = max(i for i in data if str(i**0.5)[-2:]=='.0')*3
ans = []
for num in zip(data, data[1:]):
    u1 = prod(num)**.5%1==0
    u2 = [i <=sqrt_max for i in num].count(1)>=1
    if u1+u2==2:
        ans.append(prod(num)**.5)

print(len(ans), max(ans)+min(ans))

