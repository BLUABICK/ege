with open(r'../files/24_20909.txt') as file:
    data = file.readline()

data = data.split('AB')

ans = 0

for i in range(len(data)-100):
    if i==0 or i == len(data)-3:
        ans = max(ans, len('AB'.join(data[i:i+101]))+1)
    else:
        ans = max(ans, len('AB'.join(data[i:i + 101]))+2)

print(ans)