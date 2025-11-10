def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1, 10000):
    R = convert(N, 4)
    if R[0]=='3':
        R = R.replace('1', '.')
        R = R.replace('3', '1')
        R = '21' + R.replace('.', '1')
    else:
        R = R.replace(R[0], '1') + '12'
    R = int(R, 4)
    if R <598:
        print(N)

