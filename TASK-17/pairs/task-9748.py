with open(r'..\files\17_9748.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if abs(i)%100==15)
ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = [len(str(num)) for num in nums].count(4)==1
    u2 = sum(nums) >= maxx
    if u1 * u2:
        ans.append(sum(nums))

print(len(ans), max(ans))
