with open('24_7600.txt') as file:
    data = file.readline()

cnt = 1
ans = []
for i in range(len(data)-1):
    if data[i] in 'QRS' and data[i+1] not in 'QRS' or data[i] not in 'QRS':
        cnt+=1
        ans.append(cnt)
    else:
        cnt = 1
        ans.append(cnt)

print(max(ans))