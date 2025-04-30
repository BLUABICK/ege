int() # целые числа
float() # дробные числа
complex() # пространство чисел, высшая математика, комплексный анализ
bool() # логика

# Итерируемый объект, последовательности, коллекции
list() # список
str() # строка
tuple() # кортеж

dict() # словарь
set() # множество

# Множество - тип коллекции, который содержит уникальные неиндексируемые элементы
my_set = {1, 2, 3}
# add() - добавление элемента в множество
my_set.add(4)
# принимает любой тип данных кроме списков и словарей
# возвращает ничего
print(my_set)

# remove() - удаление элемента из множества
# если передать то чего нет, будет ошибка
# возвращает ничего
my_set.remove(1)
print(my_set)

# Объединение множеств
my_set_2 = {1, 2, 3}
union_set = my_set.union(my_set_2)
print(union_set)

# Разность множеств
diff_set = my_set.difference(my_set_2)
print(diff_set)

# Симметричная разность
sym_diff_set = my_set.symmetric_difference(my_set_2)
print(sym_diff_set)

# Отношения между множествами
# issubset() - Проверяет является ли одно множество подмножеством другого
sub_set = {3, 4, 5}
super_set = {1, 2, 3, 4, 5, 6}
print(super_set.issubset(sub_set))
print(sub_set.issubset(super_set))
# issuperset() - Проверяет является ли одно множество надмножеством другого
print(super_set.issuperset(sub_set))
print(sub_set.issuperset(super_set))
