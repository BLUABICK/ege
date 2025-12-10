from itertools import product, repeat
from string import printable

cnt = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val.count('3')==1 and val[0]!=val[1] and val[1]!=val[2] and val[2]!=val[3] and val[0]!='0':
        cnt += 1
print(cnt)