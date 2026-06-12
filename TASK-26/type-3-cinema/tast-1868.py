with open('../files/26_1868.txt') as file:
    N =int(file.readline())
    seats = [list((map(int, i.split()))) for i in file.readlines()]
seats = sorted(seats)
ans = []

for i in range(len(seats)-1):
    if seats[i][0] == seats[i+1][0]:
        if seats[i+1][1]-seats[i][1]==3:
            ans.append([seats[i][0], seats[i][1]+1])

print(max(ans, key=lambda x:x[0]))