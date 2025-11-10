for N in range(1,10000):
    R = f'{N:b}'
    if N%2==0:
        R = R + bin(R.count('1'))[2:]
    else:
        R = '1' + R + '00'
    R = int(R, 2)
    if 500 < R <= 700:
        print(N)
        break
