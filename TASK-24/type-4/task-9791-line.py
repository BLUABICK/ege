with open(r'../files/24_9791.txt') as file:
    data = file.readline()

ans = cnt = i = 0
len_data = len(data)
while i < len_data:
    if int(data[i], 36) <16:
        cnt+=1
    else:
        cnt = 0
    ans = max(ans, cnt)
    i+=1
print(ans)