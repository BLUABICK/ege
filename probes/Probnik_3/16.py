from sys import setrecursionlimit
setrecursionlimit(100000)
def f(n):
    return 3*(G(n-2)+5)

def G(n):
    if n<8:
        return 3*n
    return G(n-3)+2

print(f(12345))