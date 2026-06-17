with open('../files/9_29341') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    line = sorted(i, reverse=True)

    ur_1 = min(line) + max(line)!= sum(line)-min(line)-max(line)
    ur_2 = sum(line[1:])>max(line)
    if ur_1+ur_2==2:
       cnt+=1
print(cnt)
