with open('24_28765.txt') as file:
    data = file.readline()

data = data.split('BC')
data = data
ans = []
for i in range(len(data)- 180 - 1):
    line = 'BC'.join(data[i:i + 180-1])
    ans.append(len(line))
print(max(ans))