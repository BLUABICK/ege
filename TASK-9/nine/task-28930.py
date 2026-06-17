with open('../files/9_28930') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for i in data:
    line = sorted(i)
    u1 = i[0]<i[1]<i[2]<i[3]<i[4]
    print(u1, i, line)
    u2 = line[0]+line[-1]<=sum(line[1:-1])
    if u1+u2==2:
       cnt+=1
print(cnt)
