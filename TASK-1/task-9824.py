from itertools import permutations

matrix = '346 45 16 125 247 137 56'.split()
graph = 'GD DF FA AB BC CA CE ED EG'.split()
print(*range(1,9))
for i in permutations('GDFABCE'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)