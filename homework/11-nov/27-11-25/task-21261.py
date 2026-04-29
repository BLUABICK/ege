def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(10000):
    R = convert(N, 4)
    if sum(map(int, R))%3==0:
        R = '32' + R.replace('0', '.').replace('2', '0').replace('.', '2')
    else:
        R = R[0] + '10' + R[3:] + '33'
    R = int(R,4)
    if R>320:
        ans.append([R,N])
ans.sort(key=lambda x:(x[0], -x[1]))
print(ans[0][1])

