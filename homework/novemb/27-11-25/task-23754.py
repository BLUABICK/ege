from string import  digits, ascii_lowercase
def convert2(num, sys):
    res = ''
    alph = digits + ascii_lowercase
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
for x in range(1, 3001):
    y = 9*11**210 + 8*11**150 - x
    if convert2(y, 11).count('0')==60:
        print(x)