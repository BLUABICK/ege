with open('17_21712.txt') as file:
    data = [int(i) for i in file.readlines()]

min_4_6 = min(int(i) for i in data if i>0 and len(str(i))==4 and i%10==6)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    ur_1 = (len(str(abs(num1)))==4 and str(abs(num1))[-1]=='6')  or (len(str(abs(num2)))==4 and str(abs(num2))[-1]=='6') or (len(str(abs(num3)))==4 and str(abs(num3))[-1]=='6')
    ur_2 = sum([num1, num2, num3])<=min_4_6
    if ur_2+ ur_1 ==2:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))