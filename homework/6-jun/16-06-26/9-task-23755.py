with open('9_14250.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = num = 0
for i in data:
    num+=1
    i_1 = sorted(i)
    ur_1 = len(set(i))==6
    ur_2 = (i_1[-1]-i_1[0])**3< sum(i_1[1:-1])**2
    if ur_1+ur_2==2:
        cnt += num
print(cnt)