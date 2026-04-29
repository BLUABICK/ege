from string import printable as alph
def convert2(num, sys):
    res =''
    while num:
        res+=alph[num%sys]
        num//=sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert2(N, 5)
    if R[-1]=='0':
        R = '33' + R.replace('1', '.').replace('4', '1').replace('.','4')
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R<1922:
        ans.append([R, N])
print(min(ans, key=lambda x: (-x[0], x[1]))[1])