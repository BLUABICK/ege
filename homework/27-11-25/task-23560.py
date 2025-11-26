def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(1, 2401):
    y = 7*9**210+6*9**110 - x
    if convert(y, 9).count('0')==100:
        print(x)
