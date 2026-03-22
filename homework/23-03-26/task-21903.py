with open(r'.\17_21903.txt') as file:
    data = [int(i) for i in file]

min_15 = min(i for i in data if len(str(abs(i)))==3 and abs(i)%100==15)**2

ans = []
for nums in zip(data, data[1:], data[2:]):
    if min(nums)*max(nums)>min_15:
       ans.append(min(nums)*max(nums))

print(len(ans), min(ans))
