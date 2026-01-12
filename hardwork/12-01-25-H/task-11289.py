from string import printable
from itertools import *
cnt =0
alph = printable[:9]

for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0]!='0' and '2' not in val and len(set(val))==7:
        for i in '02468':
            val = val.replace(i, '*')
        for i in '1357':
            val = val.replace(i, '.')
        if '..' not in val and '**' not in val:
            cnt+=1
print(cnt)