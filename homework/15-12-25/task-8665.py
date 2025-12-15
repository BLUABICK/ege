cnt = 0
from itertools import *
num = '0123456789ab'
for val in product(num, repeat=7):
    val = ''.join(val)
    if val[0]!='0':
        for i in '02468a':
            val = val.replace(i, '*')
        for i in '13579b':
            val = val.replace(i, '.')
        if val.count('b')==2 and '*.*.*.*' in val or '.*.*.*.' in val:
            cnt+=1
print(cnt)
# не пойму что не так
