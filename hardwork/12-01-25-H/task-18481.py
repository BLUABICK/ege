from itertools import *

matrix = '67 567 457 35 234 12 123'.split()
graph = 'AC CE EG GF FD DB BA BC DE'.split()
print(*range(1,9))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)