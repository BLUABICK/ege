with open('26_8581.txt') as file:
    N = int(file.readline())
    K = int(file.readline())
    M = int(file.readline())
    ices = [int(i) for i in file.readlines()]
ices = sorted(ices, reverse=True)
print(ices)
cameras = [M]*K
print(cameras)
cnt = 1
for ice in ices:
    for i in range(len(cameras)):
        if cameras[i]-ice>=0:
            cameras[i]-=ice
            cnt += 1
            break
        else:

            continue
print(cnt)