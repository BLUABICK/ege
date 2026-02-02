from itertools import *

matrix = '457 567 45 136 123 247 126'.split()
graph = 'EF FA AB BG GE EC CD CB DF DA'.split()
print(*range(1,9))
for i in permutations('EFABGCD'):
    if all(str(i.index(x)+1 ) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(9+2)
