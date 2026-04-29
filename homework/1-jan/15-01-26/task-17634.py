def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            for B in range(70, 91):
                f = (x%A==0) or ((B)<=(not(x%22==0)))
                if not f:
                    return False
    return True
for A in range(1, 1000):
    if f(A):
        print(A) #'эа я глупый'