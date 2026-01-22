from string import printable

alph = printable[1:8]

for x in alph:
    num1 = int(f'{x}1{x}', 16)
    num2 = int(f'{x}3{x}3', 8)
    num = num1 + num2
    for i in range(1, 15):
        if num == 2**i:
            print(x)

