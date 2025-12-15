from itertools import *
cnt = 0
for val in set(permutations('КИДАЛА', r=5)):
    val = ''.join(val)
    if 'АА' not in val and 'КК' not in val and 'ДД' not in val and 'ИИ' not in val and 'ЛЛ' not in val :
        cnt+=1
print(cnt)