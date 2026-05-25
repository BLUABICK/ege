with open(r'../files/24_28943.txt') as file:
    data = file.readline()

for i in 'EYUIOA':
    data = data.replace(i, '*')
data = data.split('*')
ans = 10**10
for line in data[:-1]:
    line = line + 'A'
    cnt_20 = line.count('20')
    if cnt_20==26:
        ans = min(ans, len(line[line.find('20'):]))
    elif cnt_20>26:
        while cnt_20>=26:
            if line[:2]=='20':
                cnt_20-=1
            line = line[1:]
        ans = min(ans, len(line)+1)
print(ans)


