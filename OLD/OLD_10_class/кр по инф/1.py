#1
from itertools import permutations
graph = 'АБ БД ДЕ ЕЖ ЖЗ ЗА ВА ВБ ВГ ГД ЕЗ'.split() #ребра без порядка
matrix = '345 35 128 156 124 478 68 367'.split()
print(*range(1,9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

#15
from  sys import setrecursionlimit
setrecursionlimit(2000)
def f(n):
    if n<110:
        return n
    return n+f(n-1)
print(f(2025)-f(2021))

#12
for N in range(4, 10_000):
    st = '1' + '2' * N
    while '12' in st or '322' in st or '222' in st:
        if '12' in st:
            st = st.replace('12', '2', 1)
        if '322' in st:
            st = st.replace('322', '21', 1)
        if '222' in st:
            st = st.replace('222', '3', 1)
    if sum(map(int, st)) == 15:
        print(N)
        break
