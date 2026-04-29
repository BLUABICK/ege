def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

for x in range(1, 1000):
    y = 7**666 + 7**333 + 49**x -343
    y = convert(y, 7)
    if y.count('6')==49:
        print(x)
        break