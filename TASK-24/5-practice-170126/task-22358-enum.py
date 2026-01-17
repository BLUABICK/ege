from string import digits, ascii_uppercase

with open(r'..\files\24_22358.txt') as file:
    data = file.readline()
alph = digits + ascii_uppercase
ans = '0'
for i in range(len(data)):
    if data[i] in alph[1:12]:
        num = data[i]
        for j in range(i+1, len(data)):
            if data[j] in alph[:12]:
                num += data[j]
                if int(num,12)%3==0 and int(num,12) > int(ans, 12):
                    ans = num
            else:
                break
print(data.find(ans))