with open('../files/26_9793.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file.readlines()]

conveyor = [0] * N
paint = []
grind = []
for i in times:
    paint.append([i[1], 'P', times.index(i) + 1])
    grind.append([i[0], 'G', times.index(i) + 1])
pain_grin = paint + grind
pain_grin = sorted(pain_grin)

n = 0
k = -1
last_piece = 0
cnt = 0
for piece in pain_grin:
    if piece[2] in conveyor:
        continue
    if piece[1] == 'G':
        conveyor[n] = piece[2]
        n += 1
        cnt += 1
    else:
        conveyor[k] = piece[2]
        k -= 1
    last_piece = piece

print(last_piece[2], cnt - 1 if last_piece[1] == 'G' else 0)

