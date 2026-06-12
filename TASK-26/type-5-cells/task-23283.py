with open('../files/26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file.readlines()]
times = sorted(times)
print(times)
windows = [0]*K
last_dow = 1
cnt = 0
for time in times:
    for i in range(len(windows)):
        if windows[i]<time[0]:
            windows[i]=time[1]
            cnt+=1
            last_dow = i+1
            break
print(cnt, last_dow)