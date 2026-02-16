from functools import *

@lru_cache(None)
def F(n):
    if n<=10:
        return n
    return n-7 + F(n-21)

for i in range(0, 185735):
    F(i)

print((F(185734) - F(185650))//F(40))