with open('9_23193.txt') as file:
    data = [list(map(int, i.split())) for i in file.readlines()]


for i in data:
    i2 = sorted(i, key=lambda x:i.count(x), reverse=True)
    u1 = len(set(i2))==4
    u2 = sum(i2[:3])/3 > sum(i2[3:])/3
    if u1+u2==2:
        print(data.index(i)+1)