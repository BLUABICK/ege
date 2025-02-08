#
# import random
# sp_sok=random.sample(range(1, 10000),100)
# max1=sp_sok[0]
# max2 = 0
# print(sp_sok)
# print(sorted(sp_sok)[-2:][::-1])
# # for i in range(0, len(sp_sok)):
# #     if sp_sok[i]>max1:
# #         max1=sp_sok[i]
# # for i in range(0, len(sp_sok)):
# #     if sp_sok[i] != max1 and sp_sok[i]>max2:
# #         max2=sp_sok[i]
# #
# # print(max1, max2)
# # print(sorted(sp_sok)[-2:][::-1])
# maxx = [0,0]
# for i in range(len(sp_sok)):
#     if maxx[0] < sp_sok[i]:
#         maxx[1] = maxx[0]
#         maxx[0] = sp_sok[i]
#     elif maxx[1]<sp_sok[i] and maxx[1]<maxx[0]:
#         maxx[1]=sp_sok[i]
# print(maxx)
from itertools import count
# import random
# sp_sok=random.sample(range(1, 10000),1000)
# print(sp_sok)
# count = 0
# for i in range(len(sp_sok)):
#     if  sp_sok[i] == sp_sok[]:
#         count +=1
#     print(count)

from random import *
len_n = 100
nums = [randint(1,100) for i in range(100)]
ans=0
for i in range(len_n - 1):
    if nums[i]==nums[i+1]:
        count =1
        for j in range(i, len_n - 1):
            if nums[j] == nums[j+1]:
                count +=1
            else:
                break
        ans = max(ans, count)
print(ans)


