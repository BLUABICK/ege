with open('26_10107.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file.readlines()]
times = sorted(times, key=lambda x:(x[1], x[0]))

last_event = times[0]

cnt=1
ans = []
for time in times:
    if last_event[1]<=time[0]:
        cnt+=1
        last_event=time
        ans.append(last_event)


ans_2 = 0
if max(times, key=lambda x: x[0])==last_event:
    ans_2 = abs(ans[-2][1]-last_event[0])

print(cnt, ans_2)