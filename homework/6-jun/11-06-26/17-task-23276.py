with open('17_23276.txt') as file:
    data = [int(i) for i in file]

max_25 = max(i for i in data if abs(i)%100==25)


ans = []
cnt = 0
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    ur_1 = (1000 <= abs(num1) <= 9999)+(1000 <= abs(num2) <= 9999)+(1000 <= abs(num3) <= 9999)<=2
    ur_2 = (num1+num2+num3)<=max_25
    if ur_2+ur_1==2:
       ans.append(num1+num2+num3)
print(len(ans), max(ans))