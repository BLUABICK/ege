# Эксперимент.
# Сравниваем время разворота списка с помощью среза s[::-1] и команды reverse().
# Вывод: используем метод reverse(), потому что он быстрее.
from timeit import timeit
from random import randint
def f1(data):
    data = data[::-1]

def f2(data):
    data.reverse()
data = []
for i in range(1000):
    data.append(randint(1, 1_000_000))

print(timeit('f2(data)', globals=globals(), number=10_000_000))
print(timeit('f1(data)', globals=globals(), number=10_000_000))