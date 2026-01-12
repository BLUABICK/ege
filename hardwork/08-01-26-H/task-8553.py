from itertools import *

pos_1 = 0
pos_2 = 0
alph = sorted('НОРМАЛЬЕ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'НОРМ' in val and val[2] == 'Р':
        pos_1 = pos
        break
    if 'НЕНОРМ' in val:
        pos_2 = pos
print(pos_1 - pos_2 - 1)
