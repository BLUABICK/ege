with open('../files/26_1207.txt') as file:
    S, N = map(int, file.readline().split())
    ssd = [int(i) for i in file.readlines()]
ssd = sorted(ssd)
cnt = 0
last = 0
ans = []
for i in ssd:
    if S>=0:
        S-=i
        cnt+=1
        l = i
        last += i
        if S-i<0:
            break
for j in ssd[ssd.index(l):]:
    if last-l+j:
        ans.append(j)
print(cnt, max(ans))