from itertools import permutations

matrix = '346 348 12 127 678 15 458 257'.split()
graph = 'DC CF FG GE EA AD AH HG HB BC BD'.split()
print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(24+23)