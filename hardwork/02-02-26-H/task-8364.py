from itertools import *

alph = sorted('КАТЕР')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val in 'КАРЕТА':
        pos_1 = pos
    if val in 'РАКЕТА':
        pos_2 = pos
print(abs(pos_1 - pos_2)-1)