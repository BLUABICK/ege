from itertools import *

alph = sorted('АПРЕЛЬ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos%2==0 and val[0] not in'ЬР' and val.count('Л')>=2:
        print(pos, val)
