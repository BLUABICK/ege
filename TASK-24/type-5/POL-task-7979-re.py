from re import *
with open(r'../files/24-314.txt') as file:
    data = file.readline()
num = r'(0|[1-7][0-7]*)'
pattern = fr'(?<=F){num}([+*]{num})+'

matches = [match.group() for match in finditer(pattern, data)]
bob = sorted(matches, key=len, reverse=True)[:2]
bob_2 = []
for line in bob:
    line = line.replace('+', ' + ').replace('*', ' * ')
    line = line.split()
    for j in range(len(line)):
        if line[j] not in '*+':
            line[j] = str(int(line[j], 8))
            ans = ''.join(line)
    bob_2.append(ans)
print(max(eval(i) for i in bob_2))