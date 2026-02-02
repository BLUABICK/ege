from itertools import product, repeat
from string import printable

cnt = 0
for val in product(printable[:8], repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('6')==1:
        for i in printable[1:8:2]:
            val = val.replace(i, '*')
        if '6*' not in val and '*6' not in val:
            cnt+=1
print(cnt)