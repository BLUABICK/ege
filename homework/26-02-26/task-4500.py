from functools import *
@lru_cache(None)

def f(a, b, c, d):
    if a==23:
        return 0
    if a==11:
        d =1
    if a>=b:
        return a==b and d==1
    if c == 1:
        return f(a+2, b, 0, d) + f(a*2, b, 0, d)
    return f(a+1, b, 1, d) + f(a+2, b, 0, d) + f(a*2, b, 0, d)

print(f(3, 79,0, 0))