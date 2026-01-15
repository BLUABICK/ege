def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (9*x+y>A) or (x>=36) or (y>=18)
            if not f:
                return False
    return True

for A in range(0, 10000):
    if f(A):
        print(A)