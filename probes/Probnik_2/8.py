from itertools import *
from string import printable

cnt_1 = 0
cnt = 0
alph = printable[:25]
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0] != 0:
        for i in range(4):
            if int(val[i], 25) <= 5:
                cnt_1 += 1
        if cnt_1 <= 2:
            for i in alph[1::2]:
                val = val.replace(i, '*')
        else:
            cnt_1 = 0
        if val.count('*') == 1:
            cnt += 1
print(cnt)
