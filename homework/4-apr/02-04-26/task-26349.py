from itertools import *

alph = sorted('СУЛАК')
for x in range(1, 10):
    for pos, val in enumerate(product(alph, repeat=x), start=1):
        val = ''.join(val)
        if val[0] in 'ЛС':
            for i in 'УА':
                val = val.replace(i, '*')
            if val.count('*')<=2 and '**' not in val and pos==12368:
                print(x)