with open('26_2944.txt') as file:
    S, N = map(int, file.readline().split())
    size = []
    for i in file:
        size.append(int(i))
size.sort()

max_size = S
cnt = 0
last_size = 0

for i in size:
    if max_size - i >= 0:
        cnt += 1
        max_size -= i
        last_size = i

size.sort(reverse=True)
max_size = max_size + last_size

for i in size:
    if max_size - i >= 0:
        last_size = i
        break
print(cnt, last_size)
