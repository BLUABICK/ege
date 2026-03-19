from math import *

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

with open(r'..\files\17_9993.txt') as file:
    data = [int(i) for i in file]
ans = []
max_17 = max(i for i in data if abs(i)%100==17)
for num in zip(data, data[1:]):
    u1 = [is_prime(i) for i in num].count(1)==1
    u2 = abs(sum(num))%max_17==0
    if u1+u2==2:
        ans.append(prod(num))

print(len(ans),max(ans))
