from itertools import permutations

matrix = '45 345 256 127 123 37 46'.split()
graph = 'FB BD DE EA AG GF BC CD CG'.split()
print(*range(1,8))
for i in permutations('FBDEAGC'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(21+30+13+2+39+8+5)