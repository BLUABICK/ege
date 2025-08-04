# Словари - тип коллекций, которых хранит в себе неиндексированный
# итерируемый набор элементов в формате "ключ:значение".
# Словари являются отдельным типом коллекций,
# который называется отображением (mapping).

my_dict = {'name':'Artyom', 'age':'16'}
print(my_dict['name'])

my_list1 = [] # создание списка
my_list2 = list()
print(type(my_list1), type(my_list2))

my_tuple1 = () # создание кортежа
my_tuple2 = tuple()
print(type(my_tuple1), type(my_tuple2))

my_set1 = {} # создание словаря
my_set2 = set()
print(type(my_set1), type(my_set2))

# keys() - все ключи словаря
print(my_dict.keys())

# values() - все значения словаря по порядку
print(my_dict.values())

# items() - все связки ключ + значение
print(my_dict.items())

# добавление элемента в словарь
my_dict['lastname'] = 'Ivanov'
print(my_dict)

# удаление элемента из словаря
a = my_dict.pop('lastname')
print(my_dict)

# извлечение элемента словаря
b = my_dict.get('age')
print(b)