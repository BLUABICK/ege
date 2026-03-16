with open(r'..\files\17_9840.txt') as file:
    data = [int(i) for i in file]

maxx = max([x for x in data if 1000<=abs(x)<=9999 and abs(x)%100==39])**2
ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = [len(str(abs(num1))), len(str(abs(num2)))].count(4)==1
    u2 = (num1+num2)**2<=maxx
    if u1+u2==2:
        ans.append(num1+num2)

print(len(ans), max(ans))