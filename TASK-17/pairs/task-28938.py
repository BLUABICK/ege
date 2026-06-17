with open('../files/17_28938.txt') as file:
    data = [int(i) for i in file.readlines()]

max_28 = max(i for i in data if abs(i)%100==28)
ans =[]
for nums in zip(data, data[1:], data[2:]):
    ur_1 = sum(len(str(abs(n)))==3 for n in nums)>=1
    ur_2 = 0<(sum(nums)/3)<max_28
    if ur_1+ur_2==2:
        ans.append(sum(nums))

print(len(ans), max(ans))