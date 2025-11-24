def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1,3001):
    y = 9**150+9**30-x
    if convert(y,9).count('0')==122:
        print(x)
        break