from itertools import *

cnt = 0
alph = sorted('НИЧЬЯ')
for val in product(alph, repeat=7):
    val = ''.join(val)
    for i in 'ИЯ':
        val = val.replace(i, '*')
    if val.count('*') == 2 and '**' not in val:
        cnt+=1

print(cnt)
