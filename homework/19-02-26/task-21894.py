from itertools import *

cnt = 0

for val in product('0123456789', repeat=4):
    val = ''.join(val)
    if val[0]!='0' and len(set(val))==4:
        for i in '02468':
            val = val.replace(i, '*')
        for i in '13579':
            val = val.replace(i, '.')
        if '**' not in val and '..' not in val:
            cnt+=1

print(cnt)