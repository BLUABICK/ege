from itertools import *
cnt=0
for val in  permutations('0123456789', r=6):
    val = ''.join(val)
    if int(val)%4==0 and val[0]!='0':
        for i in '02468':
            val = val.replace(i, '*')
        if '**' not in val:
            cnt+=1
print(cnt)