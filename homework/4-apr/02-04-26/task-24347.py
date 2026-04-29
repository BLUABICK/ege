with open(r'9_24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    maxx = line.count(max(line))==1
    coin = line[0]!=max(line)!=min(line) and line[-1]!=max(line)!=min(line)
    srt = [i for i in sorted(line)]
    print(srt)
    if srt[0] !=0:
        comp = (srt[-1]*srt[-2]*srt[-3])%min(srt)==0
        if maxx+coin+comp==1:
            cnt+=1

print(cnt)