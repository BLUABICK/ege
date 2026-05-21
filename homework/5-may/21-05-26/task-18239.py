from re import *

with open(r'24_18239.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*)'
max_len = 0

for i in range(len(data)):
    for j in range(i + 1, len(data) + 1):
        sub = data[i:j]
        if match(fr'^-?{num}(?:-{num})*$', sub):
            nums = [int(x) for x in findall(r'-?\d+', sub)]
            val = nums[0] - sum(nums[1:])
            if val > -20000:
                max_len = max(max_len, j - i)

print(max_len)
