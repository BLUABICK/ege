with open(r'files/9_27764.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    repeat = len(set([i for i in line if line.count(i)==1]))==len(line)
    srt = sorted(line)
    amount = (srt[0]+srt[-1])*2==sum(srt)-srt[0]-srt[-1]
    if repeat +amount==2:
        cnt +=1
print(cnt)