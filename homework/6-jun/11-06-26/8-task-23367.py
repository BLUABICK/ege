from string import *
from itertools import *
cnt = 0
alph = printable[:7]
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('6')==1:
        if '11' not in val and '22' not in val and '00' not in val and '33' not in val and '44' not in val and '55' not in val and '66' not in val:
            cnt+=1
print(cnt)