from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res+= alph[num%sys]
        num//=sys
    return res[::-1]
ans = []
for N in range(1, 1000):
    R = convert(N, 8)
    if R[0]=='5':
        R = R.replace('2','*').replace('1', '2').replace('*', '1')
    else:
        R = '2' + R[1:] + '10'
    R = int(R, 8)
    if R<1354:
        ans.append([N, R])
print(max(ans, key=lambda x:(x[1], x[0]))[0])