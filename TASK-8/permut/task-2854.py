from itertools import *
cnt=0
for val in set(permutations('РОСОМАХА', r=8)):
    val = ''.join(val)
    for i in 'ОА':
        val = val.replace(i, '*')
    for i in 'РСМХ':
        val = val.replace(i, '.')
    if '..' not in val and '**' not in val:
        cnt+=1
print(cnt)