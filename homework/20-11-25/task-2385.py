def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

x = 16**820-2**761+14
print(convert(x,4).count('0'))