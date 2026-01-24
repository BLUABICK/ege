from itertools import *


cnt = 0
alph = 'ТИХОРЕЦК'
a = 'ТИХО'
for val in product(alph, repeat=4):
    val = ''.join(val)
    if len(set(val)) == 4:
        cnt_1 = 0
        for i in range(0, 4):
            if val[i] == a[i]:
                cnt_1 += 1
        if cnt_1 == 2:
            for j in 'ОЕИ':
                val = val.replace(j, '*')
            if val.count('*') == 2:
                cnt += 1

print(cnt)
