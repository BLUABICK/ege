from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

x = 11*15**65+18*15**38-14*15**17+19*15**11+18338
x = set(str(x))
print(len(x))