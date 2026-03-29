with open(r'9_17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    ur = sorted(line)
    nch = sum(i for i in line if i%2!=0)
    ch = sum(i for i in line if i%2==0)
    ur1 = ur[0]< ur[1]+ur[2]+ur[3]
    ur2 = nch==ch
    if ur1+ur2==2:
        cnt+=1

print(cnt)