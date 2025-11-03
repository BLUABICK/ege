# def find_max_str_1(data):
#     cnt = 1
#     max_len = []
#     for i in range(len(data) - 1):
#         if data[i:i+2] in 'ada':
#
#             cnt = 1
#         else:
#             cnt +=1
#         max_len.append(cnt)
#     print(max(max_len))
#
#
# def find_max_str_2(data):
#     cnt = 1
#     max_len = 0
#     for i in range(len(data) - 1):
#         if data[i:i + 2] in 'ada':
#
#             cnt = 1
#         else:
#             cnt += 1
#         max_len = max(max_len,cnt)
#
#     print(max_len)
#
#
# def find_max_str_3(data):
#     data = data.replace('ad', 'a d').replace('da', 'd a')
#     data = data.split()
#     print(len(max(data, key=len)))


from timeit import timeit


def find_max_str_1(data):
    cnt = 1
    max_len = []
    for i in range(len(data) - 1):
        if data[i:i + 2] in 'ada':
            cnt = 1
        else:
            cnt += 1
        max_len.append(cnt)

    max(max_len)


def find_max_str_2(data):
    cnt = 1
    max_len = 0
    for i in range(len(data) - 1):
        if data[i:i + 2] in 'ada':
            cnt = 1
        else:
            cnt += 1
        if cnt > max_len:
            max_len = cnt


def find_max_str_3(data):
    data = data.replace('ad', 'a d')
    data = data.replace('da', 'd a')
    data = data.split()
    len(max(data, key=len))


with open('24_1866.txt') as file:
    data = file.readline()

print(timeit('find_max_str_1(data)', globals=globals(), number=100))
print(timeit('find_max_str_2(data)', globals=globals(), number=100))
print(timeit('find_max_str_3(data)', globals=globals(), number=100))
