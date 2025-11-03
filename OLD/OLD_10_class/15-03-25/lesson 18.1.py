# Список заполняется сотней псевдослучайными целыми числами в диапазоне от 0 до 1_000_000.
# Ищется среднее арифметической от значений всех элементов списка и выводится на экран.
# На экран выводится список элементов, значение которых меньше среднего арифметического.
from random import randint
#
# data = []
# length = 100
# for i in range(length):
#     data.append(randint(0, 1_000_000))
# srz = sum(data) / len(data)
#
# men = []
# for num in data:
#     if num < srz:
#         men.append(num)
# print(srz, men)


# Список заполняется сотней псевдослучайными целыми числами в диапазоне от 0 до 1_000_000.
# Напишите программу, которая выводит элементы списка,
# находящиеся между минимальным и максимальным значениями.
# data = []
# length = 10
# for i in range(length):
#     data.append(randint(-100, 1_00))
# print(data)
#
# minn = min(data)
# maxx = max(data)
# mn = data.index(minn)
# mx = data.index(maxx)
# diapz = []
# print(minn,maxx)
# for i in range(min(mn, mx)+1, max(mn, mx)):
#         diapz.append(data[i])
# print(diapz)


# Список заполняется сотней псевдослучайными целыми числами
# в диапазоне от 0 до 1_000 (включительно) и выводится на экран
# Первый и последний элемент меняются местами.
# Получившийся список выводится на экран

data = []
length = 15
for i in range(length):
    data.append(randint(0, 1_000))
print(data)
data[0], data[-1] = data[-1], data[0]
print(data)





