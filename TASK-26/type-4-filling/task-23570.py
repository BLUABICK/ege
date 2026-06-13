with open('../files/26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    powers = sorted([int(file.readline()) for i in range(N)])
    snowblowers = sorted([list(map(int, file.readline().split())) for j in range(K)], key=lambda x:(x[1], x[0]))


ams= []
ans = []
for i in range(len(powers)):
    for snow in snowblowers:
        if powers[i]<snow[0]:
            ams.append(snow[1])
            ans.append(snow)
            break


print(sum(ams), max(ans))