for N in range(1, 1000):
    R = f'{N:b}'
    R = R + str(R.count('1')%2)
    R = R + str(R.count('1') % 2)
    R = int(R, 2)
    if R>253:
        print(N)
