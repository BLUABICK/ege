from functools import *

@lru_cache(None)
def f(n):
    if n<=5: return n
    return 2*n-8+f(n-2) + f(n-1)//8

for i in range(7, 2020):
    f(i)

print(f(163))