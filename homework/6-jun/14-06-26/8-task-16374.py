from string import *
from itertools import *
cnt = 0
alph = printable[:7]
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0]!='0':
        for i in '0246':
            val =val.replace(i, '.')
        if val.count('.')==2:
            cnt+=1

print(cnt)