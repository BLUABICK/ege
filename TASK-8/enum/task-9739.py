from itertools import *

alph = sorted('МАНГУСТ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'Г' not in val and val.count('М')==2 and val[0]!='У':
        print(pos)
