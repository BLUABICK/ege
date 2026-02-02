from itertools import product, repeat
from string import printable

cnt = 0
for val in product(printable[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8')==1:
        if sum(val.count(i) for i in printable[10:15]) >= 2:
            cnt += 1
print(cnt)