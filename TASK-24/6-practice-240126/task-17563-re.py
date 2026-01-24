from re import finditer

with open(r'..\files\24_17563.txt') as file:
    data = file.readline()


pattern = r'[789][0789]*([-\*][789][0789]*)+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))