from itertools import *
cnt = 0
alph = sorted('ПРЕСТОЛ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    for i in 'ПРСТЛ':
        val = val.replace(i, '*')
    if pos%2!=0 and val[-1] in 'ЕО' and val.count('*')<=3:
        cnt+=1
print(cnt)
