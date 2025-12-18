from itertools import permutations

matrix = '256 134 267 27 16 135 34'.split()
graph = 'AF FE EC CG GD DB BA BF DE'.split()
print(*range(1,9))
for i in permutations('AFECGDB'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)