from itertools import *
cnt=0
for val in set(permutations('ХОЧУ В ВУЗ')):
    val = ''.join(val)
    if val[0] not in ' У' and ' У' not in val and val[-1] not in ' '  and '  ' not in val:
        cnt+=1
print(cnt-1)
