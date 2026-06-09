with open(r'26_20910.txt') as file:
    N, M, K = list(map(int, file.readline().split()))
    sits = [list(map(int, i.split())) for i in file.readlines()]

seats = [max(sits)[0]]*(K+1)
for i in sits:
    seats[i[1]] = min(seats[i[1]], i[0]-1)
ans = []
for i in range(len(seats)-1):
    ans.append([min(seats[i], seats[i+1]), i])
print(max(ans))