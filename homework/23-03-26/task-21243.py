def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
ans = []
for N in range(1, 1000):
    R = convert(N, 5)
    if sum(map(int,R))%5==0:
        R = R.replace('0', '*')
        R = R.replace('1', '0')
        R = R.replace('*', '1')
        R = R + '14'
    else:
        R = R + '33'
        R = '44' + R[2:]
    R = int(R, 5)
    if R>370:
        ans.append([R, N])

print(min(ans, key=lambda x: (x[0], x[1])))