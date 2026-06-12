with open('../files/26_23208.txt') as file:
    N =int(file.readline())
    details = [list(map(int, i.split())) for i in file.readlines()]

conveyor = [0]*N
paint = []
grind = []
for i in details:
    grind.append([i[0], 'G', details.index(i)+1])
    paint.append([i[1], 'P', details.index(i)+1])
process = grind+paint
process = sorted(process)

n = 0
k=-1
last_det = 0
cnt = 0
for detail in process:
    if detail[2] in conveyor:
        continue
    if detail[1]=='G':
        conveyor[n]=detail[2]
        cnt += 1
        n+=1
    else:
        conveyor[k]=detail[2]
        k-=1
    last_det = detail

print(last_det[2], cnt-1 if last_det[1]=='G' else cnt)