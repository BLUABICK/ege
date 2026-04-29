with open(r'24_8510.txt') as file:
    data = file.readline()

data = data.replace('O', '*').replace('P', '*').replace('N', '*')

data = data.replace('**', '* *')

ans = max(len(i) for i in data.split())-1
print(ans)