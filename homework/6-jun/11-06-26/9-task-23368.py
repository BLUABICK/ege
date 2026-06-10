with open('9_23368.txt') as file:
    data = [list(map(int, i.split())) for i in file.readlines()]
for i in data:
    d = sorted(i)

    u1 = len(set(i))==len(i)

    u2 = (d[0]+d[-1])*2==(d[1]+d[2]+d[3])*3

    if u1+u2==2:
        print(data.index(i)+1)