with open('24_7624.txt') as file:
    data = file.readline()

cnt = 1
ans = []
for i in range(len(data)-1):
    if data[i] in 'XYZ' and data[i+1] not in 'XYZ' or data[i] not in 'XYZ':
        cnt+=1
        ans.append(cnt)
    else:
        cnt = 1
        ans.append(cnt)

print(max(ans))