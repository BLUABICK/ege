from itertools import combinations

def f(x):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = A1 <= x <= A2
    return (Q <= R) or ((not A) <= R)

lineA = [10, 150, 160, 240, 250, 300]
linex = [11, 151, 162, 241, 251]

ans = []
for A1, A2 in combinations(lineA,2):
    if all(f(x) for x in linex):
        ans.append(A2-A1)
print(min(ans))
