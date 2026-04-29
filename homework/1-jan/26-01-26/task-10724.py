from re import finditer

with open(r'24_10724.txt') as file:
    data = file.readline()


pattern = r'[1-9A-F]+[0-9A-F]*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))