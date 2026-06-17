with open('../files/17_29971.txt') as file:
    data = [int(i) for i in file.readlines()]

max_33 = max(i for i in data if abs(i)%100==33)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    ur_1 = sum([len(str(abs(num1)))==2,len(str(abs(num2)))==2,len(str(abs(num3)))==2])==2
    ur_2 = (num1+num2+num3)**2<max_33
    if ur_1+ur_2==2:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))
