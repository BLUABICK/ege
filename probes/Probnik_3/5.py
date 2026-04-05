def convert(num,sys):
    res = ''
    while num:
        res+= str(num%sys)
        num//=sys
    return res[::-1]

for N in range(1, 1000):
    R = convert(N, 4)
    if N%4==0:
        R = R + R[:2]
    else:
        R = R + convert((N%4)*4,4)
    R = int(R, 4)
    if R>291:
        print(R, N)
        break