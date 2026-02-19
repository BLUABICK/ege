from itertools import *


def f(x):
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    A = A1 <= x <= A2
    return not (((not B) <= C) <= A)


lineA = [23, 37, 41, 73]
linex = [24, 38, 42]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all( not f(x) for x in linex):
        ans.append(A2 - A1)
print(min(ans))
