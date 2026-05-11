with open(r'../files/24_9791.txt') as file:
    data = file.readline()
for i in 'GHIJKLMNOPQRSTUVWXYZ':
    data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))