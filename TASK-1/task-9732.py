from itertools import permutations

matrix = '47 357 2567 16 236 345 123'.split()
graph = 'FC CG GA AD DB FB EC EG EF EB'.split()
print(*range(1,9))
for i in permutations('GDFABCE'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)