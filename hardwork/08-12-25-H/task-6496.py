from itertools import *

alph = 'БЕРСК'
cnt=0
for r in range(5,8):
    for val in product(alph, repeat=r):
        cnt+=1
print(cnt)
