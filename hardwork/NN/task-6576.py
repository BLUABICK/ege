from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

x=283**382+9**15+2**3
print(abs(convert2(x,14).count('b')-convert2(x,14).count('c')))