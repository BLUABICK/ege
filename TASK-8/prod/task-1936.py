from itertools import *
cnt=0
alph = sorted('ПСКАЛЬ')
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0]!='Ь' and 'ЬЬ' not in val:
        cnt+=1
print(cnt)