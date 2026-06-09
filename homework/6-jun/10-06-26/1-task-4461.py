from itertools import *
matrix = '68 568 457 35 234 12 38 127'.split()
graph = 'AB BE EF FG EG GH HA AD DC CB AB'.split()
print(*range(1, 9))
for i in permutations('BEGFHADC'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(20+45)