with open(r'26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    clients = [list(map(int, i.split())) for i in file]
clients = sorted(clients, key=lambda x: (x[0], x[1]))
wds = [0]*K
cnt = 0
for client in clients:
    for wd in range(len(wds)):
        if client[0]>wds[wd]:
            wds[wd] = client[1]
            cnt+=1
            break
        else:
            continue
print(cnt, wds)

