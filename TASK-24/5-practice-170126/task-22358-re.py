from re import *

with open(r'..\files\24_22358.txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]*'
matches = [match.group() for match in finditer(pattern, data)]

ans = '0'

for match in matches:
    if match and int(match,12)%3==0:
        if int(ans,12)< int (match,12):
            ans=match
    elif match:
        for i in range(len(match)):
            for j in range(len(match), i, -1):
                line = match[i:-j].lstrip('0')
                if line and int(match, 12) % 3 == 0:
                    if len(ans) < len(match):
                        ans = line
                        break
                    elif int(ans, 12) < int(line, 12) and len(ans) == len(line):
                        ans = line
                        break
print(data.find(ans))