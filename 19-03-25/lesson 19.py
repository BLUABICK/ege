# Решение задач со списками 2.0
# ВАРИАНТ 1
from timeit import timeit
def f1(arr):
    for i in arr:
        t1 = str(i)
        t1 = t1[1:-1]
        t1 = t1.replace(',', '')
# print(t1)
# ВАРИАНТ 2
def f2(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            j=j
#     print(arr[i][j], end=' ')
# print()

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(timeit('f1(arr)', globals=globals(), number=1_000000))
print(timeit('f2(arr)', globals=globals(), number=1_000000))