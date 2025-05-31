with open('26_20910.txt') as file:
    N,M,K = map(int, file.readline().split())
    sites = [M] * (K+1)
    for i in file:
        row, col = map(int, i.split())
        sites[col] = min(sites[col], row - 1)
print(sites)
data = []
for i in range(K):
        data.append([min(sites[i],sites[i+1]), i])

print(max(data))

