def f(x):
    P = x in range(2, 21, 2)
    Q = x in range(3, 31, 3)
    return ((x in A) <= P) and ((not Q) <= (x not in A))


A = []
for x in range(1, 100):
    if not f(x):
        A.append(x)
print(len(A))
