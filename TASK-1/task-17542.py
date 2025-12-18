from itertools import permutations

matrix = '38 58 146 36 27 347 568 127'.split()
graph = 'DE EA AH HC FG GH GB BE BD'.split()
print(*range(1,9))
for i in permutations('AFECGDBH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)