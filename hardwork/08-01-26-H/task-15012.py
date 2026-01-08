from string import printable as alph
from itertools import *

cnt = 0
for val in product(alph[:14], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val[-1] in '03' and len(set(val)) == 2:
        cnt += 1
print(cnt)
