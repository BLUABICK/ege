with open('26_17786.txt') as file:
    N, V = map(int, file.readline().split())
    V *= 1000
    weight = list(map(int, file.readlines()))

weight.sort(reverse=True)
cnt = 0
last_melon = 0

for i in weight:
    if 7000 <= i <= 12000 and V >= i:
        cnt += 1
        V -= i
        last_melon = i

print(cnt, last_melon)
