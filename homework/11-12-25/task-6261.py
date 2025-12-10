from itertools import product, repeat
from string import printable
alph = printable[:8]
cnt = 0
for val in product(alph, repeat=10):
    val = ''.join(val)
    for i in printable[1:8:2]:
        val = val.replace(i, '*')
    if val[0]!='0' and val.count('7')==5 and '*7' not in val and '7*' not in val:
        cnt += 1
print(cnt)
# тут я тупой, yt пойму он слишком долго работает


