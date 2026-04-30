with open('1_9_1.txt') as file:
    data = [list(map(int, i.split())) for i in file.readlines()]

cnt = 0
for i in data:
    u1 = sorted(i)[-1]<sum(sorted(i)[0:-1])
    u2 = i[0]+i[1]!=i[2]+i[3] and i[0]+i[2]!=i[1]+i[3] and i[0]+i[3]!=i[2]+i[1]
    if u1+u2 == 2:
        cnt+=1
print(cnt)