with open('24_19254 (1).txt') as file:
    data = file.readline()
data = data.replace('FSRQ', '*** ***')
data = data.split()
ans = 0
for i in range(len(data) - 80):
    line = ''.join(data[i:i+81]).replace('******', '****')
    ans = max(ans, len(line))

print(ans)