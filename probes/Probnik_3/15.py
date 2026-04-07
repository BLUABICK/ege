from itertools import *
ans = []
def f(x):
    P = 15<=x<=40
    Q = 21<=x<=63
    A = A1<=x<=A2
    return P<=((Q and not A)<=(not P))
lineA = [15,21, 40, 63]
linex = [16, 22, 41]
for A1, A2 in combinations(lineA, 2):
    if all(f(x)for x in linex):
        ans.append(A2-A1)
print(min(ans))