from itertools import *
from string import printable

alph = printable[10:16]
print(alph)
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] not in 'ae' and val[-1] not in 'ae':
        cnt+=1

print(cnt)