with open('../files/26_15341.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file.readlines()]
cakes = sorted(cakes, reverse=True)

last_cake = cakes[0]
cnt = 1
for cake in cakes:
    if last_cake-cake>=8:
        last_cake=cake
        cnt+=1
print(cnt, last_cake)