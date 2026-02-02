from itertools import *

alph = sorted('ГОНДУБШ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos%2!=0 and val[0]!='Б' and 'У' not in val and val.count('Н')>=2:
        print(val, pos)