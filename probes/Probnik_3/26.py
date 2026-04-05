with open('26.txt') as file:
    N = file.readline()
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: x[1])
print(data)
groups = []

for i in range(len(data)-1):
    if i[0]