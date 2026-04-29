from itertools import *

def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = A1 <= x <= A2
    return  not A or not P and Q

lineA = [23, 34, 45, 56]
linex = [25, 36, 47]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
        ans.append(A2-A1)
print(max(ans))