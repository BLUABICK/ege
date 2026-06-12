with open('../files/26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    cells = [list(map(int, i.split())) for i in file.readlines()]
cells = sorted(cells)
last_cell = 1
space_cells = [0]*K
cnt = 0
for cell in cells:
    for i in range(len(space_cells)):
        if cell[0]- space_cells[i]>=1:
            space_cells[i]=cell[1]
            cnt+=1
            last_cell = i+1
            break
print(cnt, last_cell)