from string import digits, ascii_uppercase

with open(r'..\files\24_21421.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase

for i in alph[12:]:
    data = data.replace(i, ' ')


data = data.split()

ans = 0
for i in data:
    ans = max(ans, len(i.lstrip('0').rstrip(alph[1:12:2])))
print(ans)
