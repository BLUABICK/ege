from functools import *

@lru_cache(None)
def f(n):
    if n<10:
        return n+10
    return f(n-8) + 2**n

for i in range(7, 2020):
    f(i)

print((f(4000)+2*f(3992))//f(3984))