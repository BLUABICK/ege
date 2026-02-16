from functools import *

def f(n):
    return 3*(G(n-2)+5)
@lru_cache(None)
def G(n):
    if n<8:
        return 3*n
    return G(n-3)+2

for i in range(1, 47995):
    G(i)
print(f(12345))