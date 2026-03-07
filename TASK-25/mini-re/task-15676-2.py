from itertools import *


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
       if num %i ==0:
           return True
    return False

ans = []
for l in range(1, 5):
    for N in range(10**(l-1), 10**l):
        if is_prime(N):
            for l2 in range(0, 4 - l+1):
                for Z1 in product('0123456789', repeat=l2):
                    Z1 = ''.join(Z1)
                    for l3 in range(0, 4- l-l2 +1):
                        for Z2 in product('0123456789', repeat=l3):
                            Z2 = ''.join(Z2)
                            num = int(f'1{N}03{Z1}6{Z2}')
                            if num%22768==0 and num<10**8:
                                ans.append([num, N])

for i in sorted(ans):
    print(*i)