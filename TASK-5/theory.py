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
    return res[::-1] if res else '0'

# перевод в любую систему (2 <= sys <= 36)

from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
# перевод в десятичную систему
bin_num = '101'
oct_num = '765'
tri_num = '1201'
print(int(bin_num,2))
print(int(oct_num,8))
print(int(tri_num,3))

# сумма цифр числа
# двоичное число
R_1 = '101'
sum_1 = R_1.count('1')

# число в любой системе до 10 включительно
R_2 = '198'
sum_2 = sum(map(int,R_2))

# число в любой системе до 10 включительно
R_3 = 'AF7'
sum_3 = sum(map(lambda x: int(x,36), R_3))