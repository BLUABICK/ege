def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

x = 729**8-3**18+85
print(convert(x, 9).count('0'))