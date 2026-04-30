from itertools import *

alph = sorted('АПРЕЛЬ')

for pos, val in enumerate(product(alph ,repeat=6), start=1):
    val = ''.join(val)
    if pos%2!=0 and val[0] not in 'АЛ' and val.count('П')>=2:
        print(pos, val)
        break