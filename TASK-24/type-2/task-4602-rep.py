from re import *
with open('../files/24_4602.txt') as file:
    data = file.readline()
for i in 'AO':
    data = data.replace(i, '*')
for i in 'BCD':
    data = data.replace(i, '.')
cnt = 1
data = data.split('*')
ans = []
for i in data:
    if i=='.':
        cnt+=1
    else:
        cnt = 1
    ans.append(cnt)
print(max(ans))