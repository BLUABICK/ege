from itertools import *
from string import printable

alph = printable[:16]
cnt = 0
cnt2 = 0
for val in product(alph, repeat=3):
    val = ''.join(val)
    if val[0]>val[1]>val[2]:
        cnt +=1
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0]>val[1]>val[2]>val[3]>val[4]:
        cnt2 +=1
print(cnt+cnt2)