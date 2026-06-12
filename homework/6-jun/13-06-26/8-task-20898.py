from string import *
from itertools import *
cnt = 0
alph = printable[:9]
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('0')==1:
        val = val.replace('0', '*')
        for i in '1357':
            val =val.replace(i, '.')
        if '.*'not in val and '*.' not in val:
            cnt+=1

print(cnt)