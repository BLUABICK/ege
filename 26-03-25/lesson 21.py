columns = int(input("Введите кол-во столбцов: "))
lines = int(input("Введите кол-во строк: "))

matrix = []
for i in range(lines):
    l1 = []
    while len(l1) != columns:
        if not l1:
            l2 = f'Введите {columns} чисел: '
        else:
            l2 = f'Введите правильно {columns} чисел: '

        l1 = list(map(int, input(l2).split()))
        if len(l1) == columns:
            matrix.append(l1)



# for r in range(lines):
#     matrix[r] = matrix[r][::-1]
# matrix = matrix[::-1]
for r in range(lines - 1, -1, -1):
    for g in range(columns - 1, -1, -1):
        print(matrix[r][g], end=" ")
    print()