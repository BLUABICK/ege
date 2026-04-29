def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1, 10000):
    R = convert(N, 7)
    sum_2 = sum(map(int, R))
    if sum_2%2==0:
        R = R + '555'
    else:
        R = '33' + R + '6'
    R = int(R, 7)
    if R <12717:
        print(N)