def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1, 100000):
    R = convert(N, 3)
    if sum(map(int, R)) % 2 == 0:
        R = '12' + R[2:] + '0'
    else:
        R = '10' + R[2:] + '2'
    R = int(R, 3)
    if R>105:
        print(N)
        break