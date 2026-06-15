from string import printable as alph

def convert(num, sys):
    res = ''
    while num:
        res+= alph[num%sys]
        num//=sys
    return res[::-1]

x = 3*3125**8+ 2*625**7 - 4*625**6+3*125**5-2*25**4-2025
print(convert(x, 25).count('0'))