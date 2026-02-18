from functools import *

def f(n):
    return G(n-1)+G(n-3)
@lru_cache(None)
def G(n):
    if n<=9:
        return 3*n
    return G(n-4)+2


for i in range(1, 42999):
    G(i)
print(f(42999))