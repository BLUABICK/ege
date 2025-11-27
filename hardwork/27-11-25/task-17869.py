from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

x= 3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2025
print(convert2(x, 25).count('0'))