with open('../files/24_23281.txt') as file:
    data = file.readline()

ans = 0
data = data.split('Y')
for i in range(len(data)-80):
    line = 'Y'.join(data[i:i+81])
    if line.count('2025')>=90:
        ans = max(ans, len(line))
print(ans)