with open('26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    cans = [int(i) for i in file.readlines()]
cans = sorted(cans, reverse=True)
print(cans)
summ = 0
cnt =0
for i in cans:
    if summ<=M:
        summ+=i
        cnt+=1
        if summ>M:
            cnt-=1
            summ-=i
            break
print(cnt, N-cnt)
