with open(r'..\files\26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]
passengers = sorted(passengers)
cells = [0]*K
last_cell = 0
cnt = 0

for passenger in passengers:
    for i in range(K):
        if cells[i]< passenger[0]:
            cells[i] = passenger[1]
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)