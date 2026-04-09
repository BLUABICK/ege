with open('24_28765.txt') as file:
    data = file.readline()

data = data.split('BC')
ans = []

for i in range(len(data) - 180):
    line = 'BC'.join(data[i:i + 181])
    ans.append(len(line) + 2)
print(max(ans))
