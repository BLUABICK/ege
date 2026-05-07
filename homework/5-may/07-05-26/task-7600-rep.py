with open('24_7600.txt') as file:
    data = file.readline()

for i in 'QRS':
    for j in 'QRS':
        data = data.replace(f'{i}{j}', f'{i} {j}')
data = data.split()

print(len(max(data, key=len)))