from fnmatch import *
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
       if num %i ==0:
           return True
    return False

n = []
for N in range(1, 10000):
    if is_prime(N):
        n.append(N)

for i in range(22768, 10**8+1, 22768):
    for j in n:
        if fnmatch(str(i), f'1{j}03*6*'):
            print(i, j)