with open('24_4682.txt') as file:
    data = file.readline()

for i in 'BCD':
    for j in 'BCD':
        data = data.replace(f'{i}{j}', f'{i} {j}')
for i in 'AE':
    for j in 'AE':
        data = data.replace(f'{i}{j}', f'{i} {j}')

data = data.split()
fort = [i for i in data if i[0] in 'AE']
print(len(max(fort, key=len))//2)