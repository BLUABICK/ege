def DEL(n, m):
    return n%m==0

def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = DEL(x, 128)<=((not DEL(x,A))<=(not DEL(x, 80)))
            if not f:
                return False
    return True
for A in range(320, 641):
    if f(A):
        print(A)