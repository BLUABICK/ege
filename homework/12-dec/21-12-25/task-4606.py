from itertools import permutations

matrix = '68 47 45 237 368 15 248 157'.split()
graph = 'AC CD CE DH HE EG GF FB BA AF'.split()
print(*range(1,9))
for i in permutations('ACDHEGFB'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
