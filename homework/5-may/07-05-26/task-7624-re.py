from re import *
with open('24_7624.txt') as file:
    data = file.readline()

pattern = '[XYZ]?[^XYZ]([XYZ][^XYZ]+)+[XYZ]?'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))