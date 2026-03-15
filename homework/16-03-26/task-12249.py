with open(r'.\17_12249.txt') as file:
    data = [int(i) for i in file]


ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    maxx = max(data)
    if len(str(maxx))==5 and maxx%10==3:
        u1 = abs(num1)%10==3 or abs(num2)%10==3 or abs(num3)%10==3
        u2 = num1 + num2 + num3 <= maxx
        if u1 + u2 >= 1:
            ans.append(num1 + num2 + num3)

print(len(ans), max(ans))