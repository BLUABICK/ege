from itertools import combinations


def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (B==C)

lineA = [36, 60, 75, 110]
linex = [37, 61, 76]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in linex):
        ans.append(A2-A1)
print(min(ans))
