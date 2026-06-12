with open('../files/26_10107.txt') as file:
     N = int(file.readline())
     events = [list(map(int, i.split())) for i in file.readlines()]

events = sorted(events, key=lambda x:(x[1], x[0]))
last_ev = events[0]
cnt = 1
ans =[]
for event in events:
    if event[0]-last_ev[1]>=0:
        cnt +=1
        last_ev = event
        ans.append(event)
print(cnt, abs(ans[-2][1]-ans[-1][0]))