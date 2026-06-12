with open('../files/26_17881.txt') as file:
    N = int(file.readline())
    rating = [list(map(int, i.split())) for i in file.readlines()]

rating = sorted(rating, key=lambda x:(sum(x[1:])/4,-x[0],x[1:].count(2)), reverse=True)
best_std = []
losers = []
for i in rating:
    if i[1:].count(2)==0:
        best_std.append(i)
    else:
        losers.append(i)

loser = 0
for i in rating:
    if i[1:].count(2)>2:
        loser=i[0]
        break
best_std = best_std[:(N*25//100)]
print(best_std[-1][0], loser)