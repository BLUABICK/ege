from re import *

with open(r'24_18239.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*)'
from re import *

with open("24_18239.txt") as file:
    data = file.readline()
    pattern = r"-?[1-9][0-9]*(-[1-9][0-9]*)*"
    matches = [match.group() for match in finditer(pattern, data)]
    m = 0
    for match in matches:
        nums = list(map(int, match.strip('-').split('-')))
        total_len = 0
        total_sum = 0
        l = 0
        for r in range(len(nums)):
            total_sum += nums[r]
            total_len += len(str(nums[r]))
            while total_sum - nums[l] * 2 >= 20000:
                total_sum -= nums[l]
                total_len -= len(str(nums[l]))
                l += 1
            m = max(m, total_len + r - l + (total_sum < 20000))
    print(m)