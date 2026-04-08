from itertools import permutations

matrix = '457 346 24 123 167 257 156'.split()
graph = 'АБ АВ ВЕ ЕК КД ДБ БВ ГД ГК ГЕ'.split()
print(*range(1,8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)