from string import printable as alph

cnt = set()
for x in alph[:17]:
    for y in alph[9:18]:
        if int(x,36)<int(y,36):
            num_1 = int(f'5{x}{y}A', 18)
            num_2 = int(f'18{x}7', int(y, 36))
            num = num_1 + num_2
            cnt.add(num)
print(len(cnt))