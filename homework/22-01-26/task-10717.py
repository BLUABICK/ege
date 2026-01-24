from  itertools import *

def tr(x, y, z):
    return x+y>z and x+z>y and y+z>x

def f(x):
    return not ((tr(x, 11, 18)==(not max(x,5)>68)) and tr(x, a, 5))

for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1,1000)):
        print(a)
        break