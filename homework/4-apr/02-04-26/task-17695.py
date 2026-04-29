from string import printable
from itertools import *
cnt = 0
alph = printable[:7]
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0]!='0':
        if val[0]!= val[1] and val[1]!= val[2] and val[2]!= val[3] and val[3]!= val[4]:
            for i in '345':
                val = val.replace(i, '*')
            if val.count('*')==2:
                cnt +=1
print(cnt)