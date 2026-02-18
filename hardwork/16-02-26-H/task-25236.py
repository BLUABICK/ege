from string import printable as alph
for p in range(11, 37)[::-1]:
    for x in range(2, 500000):
        num1 = int('29A1', p)
        num2 = int('47771', p)
        num3 = int('12A', p)
        num = num1+num2+num3
        if num== 1000000 + x:
            print(p)