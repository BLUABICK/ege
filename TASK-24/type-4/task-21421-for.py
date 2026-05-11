with open(r'../files/24_21421.txt') as file:
    data = file.readline().strip()

cnt = 0
checkpoint = 0
ans = []
for i in range(len(data)):
    if i<checkpoint: continue
    if 0< int(data[i], 36) < 12:
        cnt = 1
        for j in range(i+1, len(data)):
            if int(data[j], 36) <12:
                cnt+=1
            else:
                checkpoint = j
                break
            if int(data[j], 36)%2==0:
                ans.append(cnt)
print(max(ans))