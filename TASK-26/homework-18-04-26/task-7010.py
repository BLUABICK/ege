with open(r'..\files\26_7014.txt') as file:
    N = int(file.readline())
    prices = [int(file.readline()) for _ in range(N)]


max_from = [0] * N
max_from[-1] = prices[-1]
for i in range(N - 2, -1, -1):
    max_from[i] = max(prices[i], max_from[i + 1])

stock = 1
total = 0
max_daily = 0

for i in range(N):
    if i > 0:
        stock += 1

    if prices[i] == max_from[i]:
        earn = stock * prices[i]
        total += earn
        max_daily = max(max_daily, earn)
        stock = 0

print(total, max_daily)