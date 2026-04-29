for N in range(1, 10000):
    R = f'{N:b}'
    if R.count('1') % 2 == 0:
        R = '1' + R[:-2] + '10'
    else:
        R = '10' + R[2:] + '1'
    R = int(R,2)
    if R > 202:
        print(N)
        break
