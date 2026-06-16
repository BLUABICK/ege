with open('24_26078.txt') as file:
    data = file.readline()
'W*****W****W******W'
data = data.split('W')

ans = []
for i in range(1, len(data)-91):
    line = 'W'.join(data[i:i+89])
    if line.count('2025')>=110:
        ans.append(line)
print(len(min(ans, key=len)))