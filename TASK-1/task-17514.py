from itertools import permutations

matrix = '247 148 578 126 38 47 136 235'.split()
graph = 'BH HF FD DC CE CG GF GE EA AH AB'.split()
print(*range(1,9))
for i in permutations('BHFDCGEA'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)