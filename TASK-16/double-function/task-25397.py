from functools import *
@lru_cache(None)
def f(n):
    if n>40:
        return f(n-4) + 3020
    return 3*(G(n-2)-15)

@lru_cache(None)
def G(n):
    if n>=301208:
        return 10*n+50
    return G(n+7)-21

for i in range(301208, 0, -1):
    G(i)

for j in range(1, 301208):
    f(j)
print(f(2026))