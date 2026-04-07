with open(r'17_21903.txt') as file:
    data = [int(i) for i in file]

min_3 = min(i for i in data if len(str(abs(i)))==3 and abs(i)%100==15)**2
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    ur1 = (num1>0 and num2>0 and num3>0) or (num1<0 and num2<0 and num3<0)
    ur2 = min(num1, num2, num3)*max(num1, num2, num3)>min_3
    if ur1+ur2==2:
        ans.append(min(num1, num2, num3)*max(num1, num2, num3))
print(len(ans), min(ans))