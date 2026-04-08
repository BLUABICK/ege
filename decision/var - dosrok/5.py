for N in range(1, 1000):
    R = f'{N:b}'
    R = R + f'{R.count('1') % 2:b}'
    R = R + f'{R.count('1') % 2:b}'
    R = int(R, 2)
    if R>253:
        print(N)
        break