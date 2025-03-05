# def find_max_ci_1(data):
#     cnt = 1
#     max_len = []
#     for i in range(len(data)-1):
#         if data[i+1]>=data[i]:
#             cnt+=1
#         else:
#             cnt = 1
#         max_len.append(cnt)
#     print(max(max_len))
#
# def find_max_ci_2(data):
#     for i in range(9, 0, -1):
#         for j in range(i):
#             data = data.replace(f'{i}{j}', f'{i} {j}')
#
#     data = data.split()
#     print(len(max(data, key=len)))
#

from timeit import timeit

def find_max_str_1(data):
    cnt = 1
    ans = []
    for i in range(len(data) - 1):
        l1, l2 = data[i], data[i + 1]
        if l1 <= l2:
            cnt += 1
        else:
            cnt = 1
        ans.append(cnt)

    max(ans)


def find_max_str_2(data):
    for i in range(9, 0, -1):
        for j in range(i):
            data = data.replace(f'{i}{j}', f'{i} {j}')

    data = data.split()
    len(max(data, key=len))

with open('24_2393.txt') as file:
    data = file.readline()

print(timeit('find_max_str_1(data)', globals=globals(), number=100))
print(timeit('find_max_str_2(data)', globals=globals(), number=100))