def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]
ans = []
for N in range(1, 10000):
    R = convert(N, 9)
    if R[0]=='7':
        R = '34' + R.replace('6', '.').replace('3', '6').replace('.', '3')
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R< 2876:
        ans.append([R, N])
print(max(ans))