with open('26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = {}
    for i in file:
        sailor = list(map(int, i.split()))
        sailors[sailor[0]] = (sum(sailor[1:]), sailor[-1])
print(sailors)
sailors_2 = sorted(sailors, key=lambda x: (sailors[x], -x), reverse=True)

print(sailors_2)
for i in sailors_2[:S]:
    a = sailors[i]
for i in sailors_2:
    if sailors[i][0] == a[0]:
        print(i)
print(a)