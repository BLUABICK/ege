with open('24_29354.txt') as file:
    data = file.readline()
'*****B C*****B C****B C*****B C*****'
data = data.replace('BC', 'B C')
data = data.split()
ans = []
for i in range(len(data)-190):
    line = ''.join(data[i:i+191])
    ans.append(line)
print(len(max(ans, key=len)))
