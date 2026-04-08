with open(f'17.txt') as file:
    data = [int(i) for i in file]

min_p = min(i for i in data if i%23==0)
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1%min_p==0 or num2%min_p==0:
        ans.append(num1+num2)
print(len(ans), max(ans))
