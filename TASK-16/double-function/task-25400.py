from functools import *
@lru_cache(None)
def f(n):
    if n<31054:
        return f(n+4) + 3020
    return 3*(G(n-2)-15)

@lru_cache(None)
def G(n):
    if n>=28:
        return G(n-5)-15
    return 3*n-4


for i in range(0, 31056):
    G(i)

for j in range(31056, 0, -1):
    f(j)
print(f(15))