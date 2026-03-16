
from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

for p in range(31, 37):
    num1 = int('TH', p)
    num2 = int('NQ', p)
    num3 = int('U', p)
    num4 = int('1L7', p)
    if num1+num2+num3==num4:
        print(p)
