def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1, 2006)[::-1]:
    y = 4**163 * 5 + 12**62 - x
    y = convert(y, 5)
    if y.count('1')<y.count('4'):
        print(x)
        break
