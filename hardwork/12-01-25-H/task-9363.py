from itertools import *

alph = 'ХЧНБДЖТ.....'
cnt = 0
for val in permutations(alph):
    val = ''.join(val)
    if '.....' not in val:
        cnt+=1
print(cnt)