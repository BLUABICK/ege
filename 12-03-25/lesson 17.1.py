# методы обработки списков


# списки нельзя копировать как обычные переменные (числа, строки)
# При копировании списка таким образом будет происходить
# дублирование ссылки на область памяти, где хранится список
a = [1]
b = a
a += [8]
print(a,b)
print(id(b))
print(id(a))

# append()- добавление одного элемента в конце списка
test_list = [1, 2, 3]
test_list.append(5)
print(test_list)

# extend() - добавляет один список целиком в конец другого
test_list_2 = [1, 5, 7]
test_list.extend(test_list_2)
print(test_list)

# insert() - добавляет один элемент в список на определённую позицию
test_list.insert(3,4)
print(test_list)

# remove() - удаляет первый попавшийся указанный элемент из списка
test_list.remove(5)
print(test_list)

#  pop() - удаляет элемент на указанной позиции и возвращает его
test = test_list.pop(5)
print(test, test_list)

# index() - возвращает позицию указанного элемента
ind = test_list.index(1)
print(test_list,ind)

# count() - возвращает количество заданных элементов в списке
cnt = test_list.count(5)
print(test_list, cnt)

# copy() - копирует список целиком
test_list_3 = test_list.copy()
print(test_list,test_list_3)

# clear() - очищает список
test_list_3.clear()
print(test_list_3)

# sort() - сортирует список
test_list.sort()
print(test_list)

# reverse() - переворачивает список
test_list.reverse()
print(test_list)

# Математические функции
summ = sum(test_list)
minn = min(test_list)
maxx = max(test_list)
print(summ, maxx, minn)

