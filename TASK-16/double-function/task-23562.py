from functools import *

def f(n):
    return G(n-1)
@lru_cache(None)
def G(n):
    if n<=9:
        return 3*n
    return G(n-2)+1

for i in range(1, 47995):
    G(i)
print(f(47995))