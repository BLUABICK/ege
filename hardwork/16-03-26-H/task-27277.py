from string import printable as alph

from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

for N in range(1, 10000):
    R = convert(N, 3)
    if N%3!=0:
        R = '1' + R + R[-3:]
    else:
        R = R + convert(sum(map(int, str(N)))*8, 3)
    R = int(R, 3)
    if 1200<= R <= 1250:
        print(R)
