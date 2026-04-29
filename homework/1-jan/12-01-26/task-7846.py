from itertools import *


def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))

lineA = [13, 17, 19, 23]
linex = [14, 18, 21]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
       ans.append(A2-A1)
print(max(ans))
