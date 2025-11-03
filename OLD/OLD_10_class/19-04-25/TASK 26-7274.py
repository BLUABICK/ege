with open('26_7274.txt') as file:
    N = int(file.readline())
    trees = []
    for i in file:
        row, col = map(int, i.split())
        trees.append([row,col])
trees.sort()
print(trees)
cnt = 0
bob = []
for i in range(len(trees)-1):
    if trees[i][0] == trees[i+1][0]:
        if trees[i+1][1] - trees[i][1] - 1 == 13:
            bob.append(i)
print(bob, trees[bob[-1]][0],trees[bob[-1]][1]+1)
# 12



