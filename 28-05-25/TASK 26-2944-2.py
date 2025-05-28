with open('26_2944.txt') as file:
    S, N = map(int, file.readline().split())
    size = []
    for i in file:
        size.append(int(i))
size.sort()

cnt_last_size = []

for i in size:
    if S - i >= 0:
        S -= i
        cnt_last_size.append(i)
size.sort(reverse=True)
S = S + cnt_last_size.pop(-1)

for i in size:
    if S - i >= 0:
        cnt_last_size.append(i)
        break
print(len(cnt_last_size), cnt_last_size[-1])
