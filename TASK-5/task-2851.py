for N in range(1, 100000):
    R = f'{N:b}'
    P_1 = R[1::2].count('1')
    P_2 = R[::2].count('0')
    res = abs(P_1 - P_2)
    if res == 5:
        print(N)
        break
