from itertools import *


def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = A1 <= x <= A2
    return (A<=P) or Q


lineA = [43, 44, 49, 53]
linex = [43.5, 45, 50]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)
print(max(ans))
