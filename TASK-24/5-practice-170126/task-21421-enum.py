from string import digits, ascii_uppercase

with open(r'..\files\24_21421.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase

ans = 0
for i in range(len(data)):
    if data[i] in alph[1:12]:
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in alph[:12]:
                cnt+=1
                if data[j] in alph[:12:2]:
                    ans = max(ans, cnt)
            else:
                break

print(ans)