with open('1_17.txt') as file:
    data = [int(i) for i in file]


min_123 = min(i for i in data if i>0 and i%123==0)
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1+num2<min_123:
       ans.append(num1+num2)

print(len(ans), abs(max(ans)))
