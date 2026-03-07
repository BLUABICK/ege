for N in range(1, 100000):
    R = f'{N:b}'
    if N%3==0:
        R = R + R[-3:]
    else:
        R = R + f'{(N%3*3):b}'
    R = int(R, 2)
    if 120 <=R<= 135:
        print(N, R)