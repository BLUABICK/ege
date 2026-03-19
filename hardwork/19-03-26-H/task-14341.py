from string import printable

alph = printable[:22]

for x in alph:
    num1 = int(f'56{x}C20', 22)
    num2 = int(f'89F{x}2', 22)
    num3 = int(f'H24{x}K21', 22)
    num = num1+num2+num3
    if num%21==0:
        print(x, num//21)