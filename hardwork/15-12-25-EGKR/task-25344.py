def convert(num, sys):
    res = ''
    while num:
        res+= str(num%sys)
        num //=sys
    return res[::-1]

for N in range(1, 10000):
    R = convert(N, 3)
    if N%3==0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int, R))*3, 3)
    R = int(R, 3)
    if R> 208 and R%2!=0:
        print(R)