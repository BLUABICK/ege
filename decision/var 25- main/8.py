from string import printable
from itertools import *
alph = printable[:10]
cnt = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0]!='0' and len(val)==len(set(val)):
        for i in '02468':
            val = val.replace(i, '*')
        for i in '13579':
            val = val.replace(i, '.')
        if '**' not in val and '..' not in val:
            cnt+=1
print(cnt)