from functools import *
@lru_cache(None)
def f(a, b, c):
    if a%2!=0:
        c+=1
    if a>=b:
        return a==b and c<5
    return f(a+2, b, c)+ f(a+3, b, c)+ f(a*2+1, b, c)

print(f(1,625,0))