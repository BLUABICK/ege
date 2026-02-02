from itertools import product, repeat
from string import printable

cnt = 0
for val in product(printable[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and '11' not in val and \
            '22' not in val and \
            '33' not in val and \
            '44' not in val and \
            '55' not in val and \
            '66' not in val and \
            '00' not in val and \
            val.count('6')==1:
        cnt += 1
print(cnt)
