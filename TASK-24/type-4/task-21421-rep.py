from string import printable as alph
with open(r'../files/24_21421.txt') as file:
    data = file.readline().lower()

for i in alph[12:]:
    data = data.replace(i, ' ')
data = data.split()
A1 = [i for i in data if i[-1] in '02468a']
ans = []
for i in A1:
    i = i.lstrip('0')
    ans.append(i)
print(len(max(ans, key=len)))