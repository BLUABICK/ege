from string import printable as alph
from itertools import *

cnt = 0
print(alph[:6])
for val in product(alph[:6], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in '046':
            val = val.replace(i, '*')
        if '2*' not in val and '*2' not in val and '22' not in val and val.count('2')==1:
            cnt+=1

print(cnt)
