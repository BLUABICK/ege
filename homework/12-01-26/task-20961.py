from itertools import *


def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return  not (Q <= ((not A) and P) <= (not Q))

lineA = [15, 38, 142, 167]
linex = [16, 39, 143]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(not f(x) for x in linex):
        ans.append(A2-A1)
print(min(ans))