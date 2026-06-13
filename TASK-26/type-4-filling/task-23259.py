with open('../files/26_15_23259.txt') as file:
    N, M= map(int, file.readline().split())
    data = [int(i) for i in file.readlines()]
    crews = sorted(data[:N])
    sleds = sorted(data[N:])
    sleds_1 = sorted(data[N:])

cnt = 0
for crew in crews:
    for i in range(len(sleds_1)):
        if sleds_1[i]>=crew:
            sleds_1[i]*=0
            cnt+=1

last_sled = sleds[-1]
ans = 0
for crew in crews[cnt:][::-1]:
    if last_sled-crew>=0:
        ans = crew
        break
print(cnt, ans)