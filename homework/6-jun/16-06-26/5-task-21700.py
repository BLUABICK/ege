from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num%sys]
        num//=sys
    return res[::-1]

for N in range(3, 1000):
    R = convert(N, 3)
    if N%3==0:
        R = R + R[-2:]
    else:
        R = R + convert(N%3*3, 3)
    R = int(R, 3)
    if R<=150:
        print(N)
