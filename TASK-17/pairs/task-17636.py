with open(r'..\files\17_17636.txt') as file:
    data = [int(i) for i in file]

maxx = max([x for x in data if 100<=abs(x)<=999 and abs(x)%10==3])
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = sum([(len(str(abs(num1)))==3 and abs(num1)%10==3), (len(str(abs(num2)))==3 and abs(num2)%10==3), (len(str(abs(num3)))==3 and abs(num3)%10==3)])>=1
    u2 = num1+num2+num3<maxx
    if u1+u2==2:
        ans.append(num1+num2+num3)
print(len(ans),max(ans))
