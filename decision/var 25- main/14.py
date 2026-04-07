def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

for x in range(1, 2300):
    y = 7**350 + 7**150 - x
    y = convert(y, 7)
    if y.count('0')==200:
        print(x)