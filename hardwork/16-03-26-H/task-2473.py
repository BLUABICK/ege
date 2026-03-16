with open(r'.\17_2473.txt') as file:
    data = [int(i)for i in file]
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1%7==0 or num2%7==0
    u2 = abs(num1)%10==3 or abs(num2)%10==3
    if u1+u2==2:
        ans.append(num1+num2)
print(len(ans), min(ans))