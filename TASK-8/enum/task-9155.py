from itertools import *

cnt = 0
alph = sorted('АПРЕЛЬ',reverse=True)
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos<=387 and val[-1]== 'Ь':
        cnt+=1
print(cnt)