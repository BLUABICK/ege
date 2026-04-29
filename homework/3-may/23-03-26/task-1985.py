from itertools import *

alph = 'АБИКОЛУН'
ans = []
for val in permutations(alph, r=8):
    val = ''.join(val)
    for i in 'АИОУ':
        val = val.replace(i, '*')
    for i in 'БКЛН':
        val = val.replace(i, '.')
    if '**' not in val and '..' not in val:
        ans.append(val)

print(len(ans))