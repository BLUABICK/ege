from itertools import *
from string import printable

alph = printable[:7]
cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] not in'035':
        if ('22' in val and '44' not in val) or ('22' not in val and '44' in val):
            cnt+=1
print(cnt)