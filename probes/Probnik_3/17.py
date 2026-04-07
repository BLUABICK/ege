with open('17.txt') as file:
    data = [int(i) for i in file]

max_2 = max(i for i in data if len(str(i))==2)
ans = []
for num1, num2 in zip(data, data[1:]):
    ur1 = (len(str(num1))==2 and len(str(num2))!=2) or (len(str(num1))!=2 and len(str(num2))==2)
    ur2 = (num1+num2)%max_2==0
    if ur2+ur1==2:
        ans.append(num1+num2)
print(len(ans),max(ans))