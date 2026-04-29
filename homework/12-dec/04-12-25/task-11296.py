from itertools import *

alph = sorted('ДОСЖ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'Ж' and val[1] == 'С':
        print(pos)
        break