with open('24_25361.txt') as file:
    data = file.read()
from re import finditer

pattern = r'([02468](?:[13579A-EG-Z]*F){76}[13579A-EG-Z]*)'
ans = []
for x in finditer(pattern, data):
    ans.append(len(x.group(0)))
print(max(ans))