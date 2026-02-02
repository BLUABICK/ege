from itertools import *

alph = sorted('КОМПЬЮТЕР')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('К')==2 and val[0]!='Ь':
        print(pos)