with open('../files/24_20909.txt') as file:
    data = file.readline()
data = data.replace('AB', 'A B')
data = data.split()
ans = 0
for i in range(len(data) - 100):
    line = ''.join(data[i:i+101])
    ans = max(ans, len(line))

print(ans)