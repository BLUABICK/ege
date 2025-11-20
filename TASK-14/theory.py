# перевод в любую систему (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

# перевод в любую систему (2 <= sys <= 36)

from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
