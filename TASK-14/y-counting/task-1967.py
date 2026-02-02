from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

x = 3*4**38+2*4**23+4**20+3*4**5+2*4**4+1
print(convert2(x, 16).count('0'))