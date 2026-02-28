with open(r'..\files\24-367.txt') as file:
    data = file.readline()

data = data.replace('.A', ' .A')
data = data.split()

if data[0][:2]!='.A':
    data = data[1:]

if data[-1].count('.') < 2:
    data = data[:-1]
ans = 10**10
for i in range(len(data)-599):
    line = ''.join(data[i:i+599])
    last = data[i+599]
    if last.count('.')==1:
        line+=last + '.'
    else:
        pos_dot = last.find('.', 1)
        line += last[:pos_dot + 1]
    ans = min(ans, len(line))

print(ans)