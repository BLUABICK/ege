from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for x in range(27001):
    y = 3*27**9+2*27**6+27**3-x
    y = convert2(y, 27)
    if y.count('0')==6:
        print(x)
        break