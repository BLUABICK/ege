from itertools import *

def f(x):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = A1 <= x <= A2
    return (not(M or N)) == (not A)

lineA = [32, 54, 68, 76]
linex = [33, 55, 69]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
       ans.append(A2-A1)
print(max(ans))