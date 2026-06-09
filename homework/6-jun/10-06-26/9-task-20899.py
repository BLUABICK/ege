with open('9-20899.txt') as file:
    nums = [list(map(int, i.split())) for i in file.readlines()]
cnt = 0
for i in nums:
    ur_1 = max(i) < sum(sorted(i)[:3])
    ur_2 = len(set(i))==3
    if ur_1+ur_2==2:
        cnt+=1
print(cnt)