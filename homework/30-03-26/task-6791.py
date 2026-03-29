with open(r'17_6791.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if abs(i)%100==68)

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = (abs(num1)%100==68 and abs(num2)%100!=68) or (abs(num1)%100!=68 and abs(num2)%100==68)
    u2 = num1**2+num2**2>=minn**2
    if u1 + u2 == 2:
        ans.append(num1**2 + num2**2)

print(len(ans), max(ans))

