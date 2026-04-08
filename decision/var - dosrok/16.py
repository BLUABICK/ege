from sys import *

setrecursionlimit(100000000)
def f(n):
    if n<10:
        return 3
    return (n+4)*f(n-5)

print((f(257487)//683+f(257477)//67)//f(257472))