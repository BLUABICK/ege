with open('26_17643 (1).txt') as file:
    N = file.readline()
    articles = [list(map(int, i.split())) for i in file]

for i in articles:
    print(articles)