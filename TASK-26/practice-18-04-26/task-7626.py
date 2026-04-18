with open(r'..\files\26_7626.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]
time = sorted(passengers)
cells = [0]*K
last_cell = 0
cnt = 0

for pas in time:
    for i in range(K):
        if cells[i]< pas[0]:
            cells[i] = pas[1]
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)