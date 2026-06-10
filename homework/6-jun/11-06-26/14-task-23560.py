from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res+= alph[num%sys]
        num//=sys
    return res[::-1]

ans = []
for x in range(1, 2400):
    y = 7*9**210+6*9**110 - x
    y = convert(y, 9)
    if y.count('0')==100:
        ans.append(x)
print(max(ans))