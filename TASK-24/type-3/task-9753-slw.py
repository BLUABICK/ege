with open(r'..\files\24_9753.txt') as file:
    data = file.readline()

ans = cnt = l = r = 0

while r < len(data) - 1:
    if cnt <= 150:
        if data[r] == 'Y': cnt += 1
        r += 1
    else:
        if data[l] == "Y": cnt -= 1
        l += 1
    ans = max(ans, r - l - 1)

print(ans)