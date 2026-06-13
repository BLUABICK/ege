with open('../files/26_17643.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file.readlines()]

articles = {}
ans = []
for i in data:
    ans.append(i[1])
sr_buy = sum(ans)/len(ans)

for ID, price, status in data:
    if price>sr_buy:
        if ID not in articles:
            articles[ID] = [not status, price, status]
        else:
            articles[ID] = [articles[ID][0]+(not status), price,articles[ID][2]+status]


keys = sorted(articles, key=lambda x:(articles[x][0], articles[x][1], -articles[x][2]))
print(articles[keys[-1]][0]*articles[keys[-1]][1], articles[keys[-1]][2])