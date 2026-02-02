for N in range(1, 1000):
    R = f'{N+2:b}'
    R = R + str(R.count('1')%2)
    R = R + str(R.count('1')%2)
    R = int(R, 2)
    if R<61:
        print(N)