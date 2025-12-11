from string import digits, printable as alph


def pop(pom):
    pom = str(pom)
    pum = []
    for i in digits[::-1]:
        pum.append((pom.count(i)))
    pem = max(pum)
    return int(digits[::-1][pum.index(pem)])



for x in alph[1:35]:
    num_1 = int(f'6{x}QR{x}', 35)
    num_2 = int(f'{x}59SH', 35)
    num_3 = int(f'PH{x}69YW', 35)
    num = num_1 + num_2 + num_3
    if num%(pop(num)**2)==0:
        print(num/pop(num)**2)