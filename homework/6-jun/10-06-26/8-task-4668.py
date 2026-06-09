from itertools import *
from string import printable
alph = printable[:7]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0]!='0':
        if val[-1] in '3456' and val[0] in '246' and val.count('4')<=1:
            cnt+=1
print(cnt)