with open('24_6757.txt') as file:
    data = file.readline()

data = data.replace('CFE', '*')
data = data.replace('FCE', '*')
for i in 'CFE':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))