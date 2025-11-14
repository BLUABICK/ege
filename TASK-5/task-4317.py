def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1, 1000000):
    R = convert(N, 5)
    if int(R[-1])%2==0:
        R = R + '2'
    else:
        R = '2' + R + '3'
    R = int(R, 5)
    if R<1000:
        print(N)