from re import *
with open(r'..\files\24_2942.txt') as file:
    data = file.readline()

max_pairs = 0
cnt = 0
i = 0
while i < len(data) - 1:
    if data[i] == 'A' and data[i+1] in 'BC':
        cnt += 1
        i += 2
    else:
        max_pairs = max(max_pairs, cnt)
        cnt = 0
        i += 1
max_pairs = max(max_pairs, cnt)

print(max_pairs)