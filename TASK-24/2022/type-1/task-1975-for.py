with open(r'..\files\24_1975.txt') as file:
    data = file.readline()
ans = []
cnt = 1
for i in range(len(data)-1):
    if data[i]+data[i+1]!='PP':
        cnt+=1
    else:
       cnt = 1
    ans.append(cnt)
print(max(ans))