from itertools import combinations

def f(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = A1 <= x <= A2
    return D <= (((not C) and (not A)) <= (not D))

lineA = [7, 29, 68, 100]
linex = [8, 30, 99]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
       ans.append(A2-A1)
print(min(ans))