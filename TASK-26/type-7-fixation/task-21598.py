with open('../files/26_21598.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file.readlines()]

minutes = [0]*1441
for time in data:
    for i in range(time[0], time[1]+1):
        minutes[i] += 1

ans = 1
cnt = 1
for t1, t2 in zip(minutes, minutes[1:]):
    if t1 == t2:
        cnt+=1
    elif t1 != t2:
        cnt = 0
    ans = max(ans, cnt-1)

last = 0
cnt_1 = 1
cnt_2 = 0
for i in range(1, len(minutes)-1):
    if minutes[-i]!=0:
        if minutes[-i]==minutes[-i-1]:
            cnt_1 +=1
        else:
            break
    else:
        cnt_1+=1

print(1440-cnt_1, ans)
