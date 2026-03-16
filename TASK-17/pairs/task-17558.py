with open(r'..\files\17_17558.txt') as file:
    data = [int(i) for i in file]

kr_32 = len([x for x in data if abs(x)%32==0])
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1<0 or num2<0
    u2 = num1+num2<kr_32
    if u1+u2==2:
        ans.append(num1+num2)
print(len(ans), max(ans))