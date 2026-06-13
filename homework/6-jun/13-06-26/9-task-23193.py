with open('9_23193.txt') as file:
    data = [list(map(int, i.split())) for i in file.readlines()]


for i in data:
    i2 = sorted(i, key=lambda x:i.count(x), reverse=True)
    u1 = i2.count(i[0])==3 and i2.count(i[-1])==1 and i2.count(i[-2])==1 and i2.count(i[-3])==1
    u2 = sum(i2[:3])/3 > sum(i2[3:])/3
    if u1+u2==2:
        print(data.index(i)+1)