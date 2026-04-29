from itertools import *
cnt=0
for val in set(permutations('ПАРИЖАНКА')):
    val = ''.join(val)
    for i in 'АИ':
        val = val.replace(i, '*')
    if val.count('**')==1 and '***' not in val:
        cnt+=1

print(cnt)