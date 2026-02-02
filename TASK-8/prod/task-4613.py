from itertools import product, repeat
from string import printable

cnt = 0
for val in product(printable[:9], repeat=5):
    val = ''.join(val)
    if val[0] not in '01357' and val[-1] not in '18' and val.count('3')<=1:
        cnt += 1
print(cnt)