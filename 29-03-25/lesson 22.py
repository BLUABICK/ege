# сортировка
data = [9, 0, 4, -3, 8, 5]

# sorted - сортирует КОПИЮ списка
# Исходный список остаётся без изменений
data2 = sorted(data)
print(data2)

# sort - изменяет исходный список
data.sort()
print(data)
