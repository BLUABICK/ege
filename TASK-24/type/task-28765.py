with open('../files/24_28765.txt') as file:
    data = file.readline()
data = data.replace('BC', 'B C')
data = data.split()
ans = 0
for i in range(len(data)-180):
    line = ''.join(data[i:i+181])
    ans = max(ans, len(line))
print(ans)