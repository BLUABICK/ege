# Считать с клавиатуры строчку st
# Считать с клавиатуры число N
# Вывести на экран N раз строку st

# st = input()
# N = int(input())
# for i in range(N):
#     print(st)
# print()
# while N != 0:
#     N -= 1
#     print(st)

# str_num = input()
# numbers = str_num.split()
# summ = 0
# numbers2 = []
#
# for i in numbers:
#     summ += int(i)
#
# numbers2 += list(map(int, numbers))
#
# print(summ, sum(numbers2))


nums = input()
print(*map(lambda x: int(x)**2, nums.split()))