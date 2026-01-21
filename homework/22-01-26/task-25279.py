from itertools import *


def f(x):
    P = 66 <= x <= 67
    Q = 32 <= x <= 125
    T = 30 <= x <= 491
    A = A1 <= x <= A2
    return (not A) <= (P or (not Q) or (not T))

lineA = [30, 32, 66, 67, 125, 491]
linex = [31, 33, 66.5, 68, 126]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
       ans.append(A2-A1)
print(min(ans))