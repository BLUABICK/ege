from itertools import permutations

matrix = '345 35 128 156 124 478 68 367'.split()
graph = 'АБ БД ДЕ ЕЖ ЖЗ ЗА ЗЕ ГД ГВ ВБ ВА'.split()
print(*range(1,9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)