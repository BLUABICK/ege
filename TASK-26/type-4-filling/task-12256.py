with open('../files/26_12256.txt') as file:
    S, N= map(int, file.readline().split())
    packages = [int(i) for i in file.readlines()]
packages = sorted(packages)
cnt = 0
ans = []
ls_i = 0
summ = 0
for i in packages:
    if summ<=S:
        summ+=i
        ans.append(i)
        cnt+=1
        ls_i = i
    else:
        ans = ans[:-1]
        cnt-=1
        break

for j in packages:
    if ans[-1]<j and sum(ans)-ans[-1]+j<=S:
        ans = ans[:-1]+[j]
print(len(ans), ans[-1])
