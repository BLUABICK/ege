with open('../files/26_9756.txt') as file:
    N = int(file.readline())
    events = [list(map(int, i.split())) for i in file.readlines()]

events = sorted(events, key=lambda x:(x[1], x[0]))
last_event = events[0]
cnt = 1
ans = []
for event in events:
    if event[0]-last_event[1]>=0:
        cnt+=1
        last_event = event
        ans.append(event)
ans = ans[:-1]

for i in events[::-1]:
    if ans[-1][1]<=i[0]:
        ans.append(i)

print(cnt, ans[-1][1])