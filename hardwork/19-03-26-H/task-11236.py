with open(r'.\17_11236.txt') as file:
    data = [int(i) for i in file]

min_d = min(i for i in data if len(str(abs(i)))==2)**2
max_ch = max(i for i in data if len(str(abs(i)))==4 and str(i)[-1]=='1')
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = [num1>min_d, num2>min_d, num3>min_d].count(1)==2
    u2 = (abs(num1)*abs(num2)*abs(num3))%max_ch==0
    if u1+u2==2:
        ans.append(abs(num1)+abs(num2)+abs(num3))
print(len(ans), max(ans))