with open('26_3664.txt') as file:
    N = int(file.readline())
    trees = []
    for i in file:
        row, col = map(int, i.split())
        trees.append([row,col])
trees.sort()
print(trees)
cnt = 0
max_col = []
for i in range(N-1):
    if trees[i][0] == trees[i+1][0]:
        cnt = trees[i+1][1] - trees[i][1] - 1
        max_col.append([cnt, trees[i][0]])
print(max(max_col))
