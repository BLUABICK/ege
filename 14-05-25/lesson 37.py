# Функции
# структура
# def <название функции>(<параметр1>, <параметр2>, ...)
def error(massage):
    print('You have', massage, 'error')


# вызов функции
# в функцию передаются аргументы
error('Value')


# Если мы хотим задать значение по умолчанию
# делаем это при объявлении параметров функции
def welcome_print(name='User'):
    print('Hello', name)

welcome_print()

# args - сокращение от слова arguments(аргументы)
# позволяет передать в функцию произвольное кол-во аргументов
# * - команда распаковки
def print_sum(*args):
    my_sum = 0
    for i in args:
        my_sum += i
    print(my_sum)

print_sum(1, 2, 3, 4, 5)


#kwargs - сокращение от слов key word arguments (именованные аргументы)
# ** - сопоставление ключей из словаря и названий переменных в функции
def print_client_data(name, surname, age, address):
    print('Имя клиента:', name)
    print('Фамилия клиента:', surname)
    print('Возраст клиента:', age)
    print('Адрес клиента:', address)

client1 = {'name':'Artem', 'surname':'Nesterenko', 'age':17, 'address':'KLGD'}
client2 = {'name':'Artem', 'surname':'Shigrev', 'age':16, 'address':'KLGD'}
client3 = {'name':'Artem', 'surname':'Mishunov', 'age':16, 'address':'KLGD'}

print_client_data(**client1)