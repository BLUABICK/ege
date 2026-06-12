with open('../files/26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file.readlines()]

enrollments = [0]*N
candidates = {}
for i in data:
    candidates[i[0]] = i[1:]
candidates = sorted(candidates.items(), key=lambda x:(sum(candidates[x[0]][:-1]), candidates[x[0]][-1]), reverse=True)


score05 = 0
for candidate in candidates:
    for i in range(len(enrollments)):
        if not enrollments[i]:
            enrollments[i] = sum(candidate[1][:-1])
            break

score = enrollments[:S][-10]
score05 = enrollments[S:][0]

cnt =0
for candidate in candidates:
    if sum(candidate[1][:-1])==score05:
        cnt+=1
last = 0
for candidate in candidates[::-1]:
    if sum(candidate[1][:-1])==score and candidate[1][-1] == min(candidate[1]):
        last = candidate[0]
        break
print(last, cnt)