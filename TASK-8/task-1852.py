from itertools import *
cnt=0
alph = sorted('ГЕПАРД')
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('Г')==1 and val[0]!='А' and val[-1]!='Е':
        cnt+=1
print(cnt)