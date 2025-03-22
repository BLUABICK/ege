# from random import randint, choice, choices, sample
from math import sqrt
#
# #
# # data = []
# # corni = []
# # for i in range(15):
# #     data.append(randint(1, 100))
# # print(data)
# # # for i in data:
# # #     corni.append(sqrt(i))
# # # print(corni)
# #
# # corni2 = list(map(sqrt, data))
# # print(corni2)
#
# data = [3, 4, 5, 6]
# print(choices(data,k=3))
# print(sample(data,k=3))
from random import randint
# data = []
# data2 = []
# for i in range(15):
#      data.append(randint(32, 127))
#
# for i in data:
#     data2.append(chr(i))
# print(data2)
#
# data3 = []
#
# for i in data2:
#     d = i * randint(1,20)
#     data3.append(d)
# print(data3)
#
# print(list(map(len, data3)))

data = []
data2 = []
for i in range(10):
     data.append(randint(0, 9))

print(data)

for i in data:
    d = str(i) * randint(1, 20)
    data2.append(d)
d2 = list(map(int, data2))
print(data2)
print(list(map(sqrt, d2)))


