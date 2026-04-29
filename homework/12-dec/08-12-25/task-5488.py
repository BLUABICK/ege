from itertools import *

alph = sorted('ПОЛИНА')
cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    for i in 'ОИА':
        val = val.replace(i, '*')
    for j in 'ПЛН':
        val = val.replace(j, '.')
    if val.count('.') > val.count('*'):
        cnt += 1
print(cnt)
