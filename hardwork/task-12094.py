for N in range(1, 10000):
    R = f'{N:b}'
    if N%8==0:
        R = R + R[-2:]
    else:
        R = R + f'{N%8*2:b}'
    R = int(R, 2)
    if R > 3000:
        print(N)
        break