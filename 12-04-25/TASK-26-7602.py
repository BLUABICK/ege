with open('26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times.sort()
print(times)
cnt = 0
cells = [0] * K
last_cell = 1
for time in times:
    for i in range(K):
        if time[0] >= cells[i]:
            cells[i] = time[1] + 1
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)
