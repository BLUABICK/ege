from string import printable as alph

print(alph)
for p in range(34, 37):
    num1 = int('kot', p)
    num2 = int('golodni', p)
    num3 = int('meeow', p)
    num4 = int('100', p)
    num5 = int('420194023088')
    num = num1+num2+num3+num4+num5
    if num:
        print(p, int('purr', 36), num)

