from sys import *

setrecursionlimit(10000)
def f(n):
    return 2*(G(n-3)+8)

def G(n):
    if n<10:
        return 2*n
    return G(n-2)+1

print(f(15548))