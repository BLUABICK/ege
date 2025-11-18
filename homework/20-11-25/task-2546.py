from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

x = 4**36+3*4**20+4**15+2*4**7+49

print(len(set(convert2(x, 16))))