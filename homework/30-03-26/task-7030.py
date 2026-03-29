with open(r'9_7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    repeat = sorted(line.count(i) for i in set(line)).count(2)==3
    if repeat:
        triangle = sorted(i for i in set(line))
        if triangle[0]**2==triangle[1]**2+triangle[2]**2 or triangle[1]**2==triangle[0]**2+triangle[2]**2 or triangle[2]**2==triangle[1]**2+triangle[0]**2:
            cnt+=1


print(cnt)