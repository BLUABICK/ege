# системы счисления
N = 25
# двоичная система
print(bin(N)[2:])
print(f'{N:b}')

# восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

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
# перевод в десятичную систему
bin_num = '101'
oct_num = '765'
tri_num = '1201'
print(int(bin_num,2))
print(int(oct_num,8))
print(int(tri_num,3))