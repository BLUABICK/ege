from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2301):
    y = 7**350+7**150-x
    y = convert2(y, 7)
    if y.count('0')==200:
        print(x)

