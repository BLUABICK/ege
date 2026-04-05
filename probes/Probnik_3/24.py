with open('24.txt') as file:
    file = file.readline()
data = file.split('Z')
ans = []
for i in range(len(data) - 270 -1):
    line = 'Z'.join(data[i:i + 270 -1])
    ans.append(len(line))
print(min(ans))
