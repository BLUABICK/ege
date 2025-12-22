from itertools import product
from string import printable
alph = printable[:7]
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0]!='0' and val[-1] in '456':
        for i in '0246':
            val = val.replace(i, '*')
        if val.count('*')==3:
            cnt+=1
print(cnt)
