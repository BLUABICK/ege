from itertools import *
from string import printable
cnt = 0
alph = printable[:7]
for val in product(alph,repeat=5):
    val = ''.join(val)
    if val[0]!='0':
        for i in val:
            if str(int(i)%10) in '0246':
                val = val.replace(i, '*')
        if val.count('**')>=2 and val.count('***')==0:
            cnt+=1
print(cnt)