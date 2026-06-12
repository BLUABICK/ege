with open('../files/26_9847.txt') as file:
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file.readlines()]

minutes = [0]*1440
cnt = 0
for time in times:
    for i in range(time[0], time[1]):
        minutes[i] +=1
for i in range(len(minutes)-1):
    if minutes[i]==minutes[i+1]==max(minutes):
        cnt+=1

print(cnt, max(minutes))