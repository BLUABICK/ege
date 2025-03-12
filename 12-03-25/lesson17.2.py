data = input()
data = data.split()
cnt = 0
print(data)
for i in range(len(data)):
    if data[i].count('-')%2!=0:
        cnt+= 1
print(cnt)