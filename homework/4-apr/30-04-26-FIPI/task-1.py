from itertools import *

matrix = '27 1567 67 5 246 2357 1236'.split()
graph = 'ГВ ВБ БА БД ДК КЕ ЕГ ВЕ ЕД ВД'.split()

print(*range(1,8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(9)
