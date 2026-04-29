from itertools import *

alph = sorted('ДИОНИСИЙ')
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if (val.count('Д')>=1 or val.count('Н')>=1) and val[0]!='Р' and val[-1] not in 'ЛГРТМ':
        cnt +=1
print(cnt)
# у меня др я немного запутался пойду отмечать, извините