from itertools import *

matrix = '234 136 12 457 467 25 45'.split()
graph = 'FB BD DA AE EC CG GF FD GE'.split()
print(*range(1, 8))
for i in permutations('FBDAECG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print('37')