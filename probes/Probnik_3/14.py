from string import printable as alph1
print(len('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
print(alph1[:39])
alph = alph1[:39]

def convert(num, sys):
    res = ''
    while num:
        res += alph[num%sys]
        num//=sys
    return res[::-1]
ans = []
for x in range(1, 9431):
    y= 39**483+39**235 - x
    y = convert(y, 39)
    ans.append(y.count('0'))
print(max(ans))




