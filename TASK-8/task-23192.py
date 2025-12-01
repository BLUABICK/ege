from itertools import *

alph = sorted('ТЕОРИЯ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'РТЯ' and val.count('И')>=2:
        if pos%2!=0:
            print(pos)