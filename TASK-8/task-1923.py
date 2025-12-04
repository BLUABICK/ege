from itertools import *

cnt = 0
alph = sorted('ПИТОН')
for val in product(alph, repeat=4):
    val = ''.join(val)
    for i in 'ИО':
        val = val.replace(i, '*')
    for i in 'ПТН':
        val = val.replace(i, '.')
    if val.count('*') == 2 and '**' not in val and val.count('.')==2 and '..' not in val:
        cnt+=1

print(cnt)