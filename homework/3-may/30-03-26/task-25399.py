from functools import *
from sys import *

setrecursionlimit(1000000)
def f(n):
    if n>=128:
        return f(n-5)+1092
    return 5*G(n-7)+29

def G(n):
    if n>303728:
        return n-15
    return G(n+8)//2-109

print(f(2049))