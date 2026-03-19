with open(r'..\files\17_2997.txt') as file:
    data = [int(i) for i in file]

data_3zn = [int(str(abs(i))[1]) for i in data if len(str(abs(i)))==3]
most = max([(data_3zn.count(i), i) for i in set(data_3zn)])[1]
ans = []
for num1, num2 in zip(data, data[1:]):
    if [str(abs(num1))[-1]==str(most), str(abs(num2))[-1]==str(most)].count(1)>=1:
        ans.append(num1+num2)

print(len(ans), max(ans))
