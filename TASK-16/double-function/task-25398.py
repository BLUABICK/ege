from functools import *
@lru_cache(None)
def f(n):
    if n>30:
        return f(n-6) + 2048
    return 3*(G(n-5)+13)

@lru_cache(None)
def G(n):
    if n>=221337:
        return 2*n+50
    return G(n+11)-48

for i in range(221337, 0, -1):
    G(i)

for j in range(1, 221337):
    f(j)
print(f(5078))