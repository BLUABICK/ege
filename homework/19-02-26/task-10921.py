from itertools import *

cnt = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    if val.find('А') + val.index('И') + val.rfind('А') + 3 == 11:
        cnt += 1
print(cnt)