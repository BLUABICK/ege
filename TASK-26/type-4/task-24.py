with open('../files/26_24.txt') as file:
    S, N = map(int, file.readline().split())
    ssd = [int(i) for i in file.readlines()]
ssd = sorted(ssd)
cnt= 0
last = []
print(ssd)
for i in ssd:
    if S>=0:
        S-=i
        cnt += 1
        last.append(i)
        if S - i < 0:
            break


print(cnt, max(last)+21)

