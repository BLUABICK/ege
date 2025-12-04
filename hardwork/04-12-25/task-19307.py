def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

x = 15625**16-3125**3*25**19+625**4-2005
print(convert(x, 5).count('0'))