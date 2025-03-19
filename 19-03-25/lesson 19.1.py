#Задача 2
# columns = int(input('Введите количество столбцов:'))
# lines = int(input('Введите количество строк:'))
# matrix = []
# for i in range(lines):
#     matrix.append([0]*columns)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()

# Задача 3
columns = int(input('Введите количество столбцов:'))
lines = int(input('Введите количество строк:'))
matrix = []
for i in range(lines):
    test = list(map(int, input('Введите ' + str(columns) + ' числа:').split()))
    matrix.append(test)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()




