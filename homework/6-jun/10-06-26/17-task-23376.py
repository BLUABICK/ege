with open('17_23376.txt') as file:
    data = [int(i) for i in file]

max_37 = max(i for i in data if len(str(abs(i)))==5 and abs(i)%100==37)**2
ans = []
for num1, num2 in zip(data, data[1:]):
    ur_1 = len(str(abs(num1)))==5 and len(str(abs(num2)))!=5 or len(str(abs(num2)))==5 and len(str(abs(num1)))!=5
    ur_2 = (num1+num2)**2>max_37
    if ur_1+ur_2==2:
       ans.append(num1+num2)
print(len(ans), max(ans))
