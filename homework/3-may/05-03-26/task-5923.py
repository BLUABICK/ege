from itertools import *

def f(x):
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = A1 <= x <= A2
    return (Q <= P) or ((not A)<=R)

lineA = [5, 280, 295, 375, 400, 450]
linex = [6, 288, 296, 376, 401]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
       ans.append(A2-A1)
print(min(ans))