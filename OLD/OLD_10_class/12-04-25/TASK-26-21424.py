with open('26_21424.txt') as file:
    N = int(file.readline())
    sizes = [int(i) for i in file]
print(sizes)
sizes.sort(reverse=True)
print(sizes)
last = sizes[0]
cnt = 1
for i in sizes:
    if last - i >= 9:
        last = i
        cnt +=1


print(cnt, last)