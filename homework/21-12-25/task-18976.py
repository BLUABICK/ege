from string import printable
from  itertools import *
cnt = 0
alph = printable[:20]

for val in product(alph, repeat=5):
    val = ''.join(val)

    if val[0] != '0' and int(val[0], 20) + int(val[-1], 20)==26:
        for i in '02468acegi':
            val = val.replace(i, '*')
        for i in '13579bdfhj':
            val = val.replace(i, '.')
        if '**' not in val and '..' not in val:
            cnt+=1
print(cnt)