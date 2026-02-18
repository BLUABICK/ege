from functools import *
@lru_cache(None)
def f(n):
    if n>=128:
        return f(n-5) + 1092
    return 5*G(n-7)+29

@lru_cache(None)
def G(n):
    if n>=303728:
        return n-15
    return G(n+8)/2-109

for i in range(301208, 0, -1):
    G(i)

for j in range(1, 301208):
    f(j)
print(f(2026))