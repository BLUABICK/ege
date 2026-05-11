with open(r'../files/24_9791.txt') as file:
    data = file.readline()

cnt = 0
ans = []
for i in data:
    if int(i, 36)<= int('F', 16):
        cnt+=1
    else:
        cnt = 0
    ans.append(cnt)
print(max(ans))