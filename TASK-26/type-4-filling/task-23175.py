with open('../files/26_2_23175.txt') as file:
    N, M = map(int, file.readline().split())
    data = [int(i) for i in file.readlines()]
    weights = data[:N]
    lifting = data[N:]

weights = sorted(weights)
lifting = sorted(lifting)

ans = []
cnt = 0
max_lift = lifting[-1]
for i in weights:
    for j in range(len(lifting)):
        if lifting[j] - i >= 0:
            ans.append([lifting[j] - i, i])
            lifting[j] -= i
            cnt += 1
            break
ans_2= 0
for i in weights:
    if i==max_lift:
        ans_2 = max_lift-ans[-1][1]

print(cnt, ans_2)
