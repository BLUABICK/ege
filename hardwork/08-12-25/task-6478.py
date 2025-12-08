from itertools import *

alph = 'МОЛЬ'
cnt=0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0]!='Ь' and 'ОЬ' not in val and 'ЬЬ' not in val:
        cnt+=1
print(cnt)
