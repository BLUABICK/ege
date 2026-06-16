with open('26_7274.txt') as file:
    N = int(file.readline())
    seeds = [list(map(int, i.split())) for i in file.readlines()]

seeds = sorted(seeds)
ans = []
for i in range(len(seeds)-1):
    if seeds[i+1][0]==seeds[i][0]:
        if seeds[i+1][1]-seeds[i][1]==14:
            ans.append([seeds[i][0], seeds[i][1]+1])

print(max(ans))