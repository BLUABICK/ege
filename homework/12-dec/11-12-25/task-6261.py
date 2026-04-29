from itertools import product, repeat
from string import printable
alph = printable[:8]
cnt = 0
for val in product(alph, repeat=10):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 5:
        for i in printable[1:6:2]:
            val = val.replace(i, '*')
        if '*7' not in val and '7*' not in val and '77' not in val:
            cnt += 1
print(cnt)



