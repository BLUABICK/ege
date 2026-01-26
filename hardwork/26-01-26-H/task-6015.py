from itertools import *
from string import printable

alph = printable[:9]

cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0]!='0':
        if val[0] not in '1357' and val[-1] not in '02468' and val.count('8')==1:
            cnt+=1

print(cnt)