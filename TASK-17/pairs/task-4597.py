with open(r'..\files\17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn
    if u1 + u2 >= 1:
        ans.append(num1 + num2)

print(len(ans), max(ans))

