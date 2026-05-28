from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res+= alph[num%sys]
        num//=sys
    return res[::-1] if res else '0'
ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if N%3==0:
        R = R + R[-2:]
    else:
        R = R + convert(N%3*5, 3)
    R = int(R, 3)
    if R>150:
        ans.append(R)
print(min(ans))