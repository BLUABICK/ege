from string import *
from itertools import *
cnt = 0

alph = printable[:8]

for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0]!='0' and len(set(val))==6 and int(val, 8)%5==0:
        for i in '0246':
            val = val.replace(i, '*')
        for i in '1357':
            val = val.replace(i, '.')
        if '**' not in val and '..' not in val:
            cnt+=1

print(cnt)
