with open('24_26078.txt') as file:
    data = file.readline()
'***W*****W****W******W****W******W'
data = data.split('W')

ans = []
for i in range(1, len(data)-89):
    line = 'W' + 'W'.join(data[i:i+89]) + 'W'
    if line.count('2025')>=110:
        ans.append(line)
print(len(min(ans, key=len)))