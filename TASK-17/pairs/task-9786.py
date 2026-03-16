with open(r'..\files\17_9786.txt') as file:
    data = [int(i) for i in file]

maxx = max([x for x in data if abs(x)%100==25])
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = [len(str(abs(num1))), len(str(abs(num2))), len(str(abs(num3)))].count(4)<=2
    u2 = num1+num2+num3 <=maxx
    if u1+u2 == 2:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))
