with open('24_7624.txt') as file:
    data = file.readline()

for i in 'XYZ':
    for j in 'XYZ':
        data = data.replace(f'{i}{j}', f'{i} {j}')
data = data.split()

print(len(max(data, key=len)))