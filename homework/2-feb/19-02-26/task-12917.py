from itertools import *
cnt=0
for val in set(permutations('ПРОСТО')):
    val = ''.join(val)
    if 'ПП' not in val and 'ОО' not in val and 'РР' not in val and 'СС' not in val and 'ТТ' not in val:
        cnt+=1
print(cnt)