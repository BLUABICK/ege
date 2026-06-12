with open('../files/26_23383.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file.readlines()]

dots = {}

for i in data:
    if i[1] in dots:
        dots[i[1]] |= {i[0]}
    else:
        dots[i[1]] = {i[0]}
ans = []
for i in dots.items():
    an = [i[0], i[1]]
    an[1] = sorted(an[1])
    ans.append(an)
ans = sorted(ans, key=lambda x:(len(x[1])))

last = []
for dot in ans:
    cnt = 1
    for i in range(len(dot[1])-1):
        if dot[1][i+1]-dot[1][i]==1:
            cnt+=1
            last.append([cnt, dot[0]])
        else:
            cnt = 1
print(max(last, key=lambda x: (x[0], -x[1])))

