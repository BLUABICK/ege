from itertools import *
from string import printable

alph = printable[:8]
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0]!='0' and '3' not in val and len(set(val))==6:
        for i in '0246':
            val = val.replace(i, '.')
        if '..' in val:
            cnt+=1
print(cnt)