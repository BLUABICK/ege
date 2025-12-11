from itertools import *
cnt=0
for val in  permutations('ПРОБНИК'):
    val = ''.join(val)
    if val[0] in 'ПРБНК' and val[-1] in 'ПРБНК' and 'ОИ' not in val and 'ИО' not in val:
        cnt+=1
print(cnt)