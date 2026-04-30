from itertools import *


def f(x):
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    A = A1 <= x <= A2
    return (not A)<=(B==C)

lineA = [22, 32, 40, 50]
linex = [23, 33, 41]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
       ans.append(A2-A1)
print(max(ans))