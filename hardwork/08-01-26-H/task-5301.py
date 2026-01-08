from itertools import *

alph = sorted('ЛЕСЯ ')
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    for i in 'ЕЯ':
        val = val.replace(i, '*')
    for i in 'ЛС':
        val = val.replace(i, '.')
    if '**' not in val and '..' not in val and val[0] != ' ' and val[-1] != ' ' and val.count(' ')==1:
        cnt += 1
print(cnt)
