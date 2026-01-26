from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

for p in range(25, 37):
    num_1 = int('bo', p)
    num_2 = int('om', p)
    num_3 = int('bl4', p)
    num_4 = int('cng', p)
    if num_4==num_1+num_2+num_3:
        print(p)