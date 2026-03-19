from itertools import *
from string import printable

alph = printable[:16]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('6')==2 and val[0]!='0':
        val = val.replace('6', '.')
        for i in alph[:16:2]:
            val = val.replace(i, '*')
        if '.*' not in val and '*.' not in val and '..' not in val:
            cnt+=1
print(cnt)