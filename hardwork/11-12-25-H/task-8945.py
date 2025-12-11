from itertools import product, repeat
from string import printable as alph

cnt = 0
for val in product(alph[:12], repeat=7):
    val = ''.join(val)
    if val[0]!='0':
        for i in '0369':
            val = val.replace(i, '*')
        for j in '124578ab':
            val = val.replace(j, '.')
        if '*.*.*.*' in val or '.*.*.*.' in val :
            cnt+=1
print(cnt)