from string import printable as alph
for x in alph[:29]:
    y1 = int(f'923{x}874', 29)
    y2 = int(f'524{x}6152', 29)
    y = y1+y2
    if y%28==0:
        print(y//28, x)
