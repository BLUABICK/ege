with open('../files/24-280.txt') as file:
    data = file.readline()
data = data.replace('X', ' ').replace('Y', ' ')
data = data.split()
ans = 0
for line in data:
    cnt_S = cnt_U = cnt_N = 0
    l = 0
    for r in range(len(line)):
        if line[r]=='S': cnt_S+=1
        if line[r]=='U': cnt_U+=1
        if line[r]=='N': cnt_N+=1
        while cnt_S>10 or cnt_U >10 or cnt_N>10:
            if line[l] == 'S': cnt_S -= 1
            if line[l] == 'U': cnt_U -= 1
            if line[l] == 'N': cnt_N -= 1
            l+=1
        ans = max(ans, r-l+1)

print(ans)