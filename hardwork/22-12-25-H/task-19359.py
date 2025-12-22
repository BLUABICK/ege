from string import printable as alph

for x in alph[:22]:
    num_1 = int(f'A23{x}AC0', 22)
    num_2 = int(f'GB{x}21670', 22)
    num = num_1+num_2
    if num%21==0:
        print(x, num//22)