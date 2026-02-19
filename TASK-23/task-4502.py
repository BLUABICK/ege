
def f(a, b):
    if b > a:
        return 0
    if a == b:
        return 1
    N = f(a + 1, b) + f(a + 2, b) + f(a * 2, b)
    if N ==6:
        return N
    return 0

for i in range(34, 60):
