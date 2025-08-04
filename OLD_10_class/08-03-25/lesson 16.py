# from timeit import timeit
#
#
# def find_max_len_of_str_1(data):
#     alph = 'EYUIOA'
#
#     cnt = 1
#     ans = 0
#     for i in range(len(data) - 1):
#         if data[i] in alph and data[i + 1] not in alph or \
#                 data[i] not in alph and data[i + 1] in alph:
#             cnt += 1
#         else:
#             cnt = 1
#         if ans < cnt:
#             ans = cnt
#
#
# def find_max_len_of_str_2(data):
#     glas = 'EYUIOA'
#     sogl = 'QWRTPSDFGHJKLZXCVBNM'
#
#     for i in sogl:
#         for j in sogl:
#             data = data.replace(f'{i}{j}', f'{i} {j}')
#
#     for i in glas:
#         for j in glas:
#             data = data.replace(f'{i}{j}', f'{i} {j}')
#
#     data = data.split()
#
#     len(max(data, key=len))
#
#
# def find_max_len_of_str_3(data):
#     glas = 'EYUIOA'
#     sogl = 'QWRTPSDFGHJKLZXCVBNM'
#
#     for i in glas:
#         data = data.replace(i, '1')
#
#     for i in sogl:
#         data = data.replace(i, '0')
#
#     while '00' in data or '11' in data:
#         data = data.replace('11', '1 1')
#         data = data.replace('00', '0 0')
#
#     data = data.split()
#
#     len(max(data, key=len))
#
#
# with open('24_11813.txt') as file:
#     data = file.readline()
#
# print(timeit('find_max_len_of_str_1(data)', globals=globals(), number=1))
# print(timeit('find_max_len_of_str_3(data)', globals=globals(), number=1))
# print(timeit('find_max_len_of_str_2(data)', globals=globals(), number=1))

# data = input()
# data = data.replace('AXMM', 'AXM XMM')
# data = data.split()
# print(data)
# print(len(max(data, key=len)))
