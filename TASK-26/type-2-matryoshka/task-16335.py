with open('../files/26_16335.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file.readlines()]
cakes = sorted(cakes, reverse=True)

last_cake = cakes[0]
cnt = 1
for i in cakes:
    if last_cake-i>=4:
        last_cake=i
        cnt+=1
print(cnt, last_cake)