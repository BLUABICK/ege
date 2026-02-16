from itertools import *

alph = sorted('СДАЙЕГЭ')
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'ЕГЭ' in val:
        cnt+=pos
print(cnt)