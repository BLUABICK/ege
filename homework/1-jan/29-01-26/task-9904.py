from string import printable

alph = printable[14:14]
alph_2 = printable[1:14]
for x in alph:
    for y in alph_2:
        num_1 = int(f'7{x}37{y}', 14)
        num_2 = int(f'9{y}63', int(x, 14))
        num_3 = int(f'15148', int(y, 14))
        num = num_1 + num_2 - num_3
        print(num)
