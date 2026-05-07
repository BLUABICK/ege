with open(r'../files/24_1975.txt') as file:
    data = file.readline()

ans = 0
cnt = 1
i = 0
while i < len(data)-1:
    if data[i] == 'P' and data[i+1] == 'P':
        cnt = 1

    else:
        cnt += 1
    i += 1
    ans = max(ans, cnt)
print(ans)