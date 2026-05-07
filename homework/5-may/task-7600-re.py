from re import *
with open('24_7600.txt') as file:
    data = file.readline()

pattern = '[^QRS]*([QRS][^QRS]+)+[QRS]?'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)), max(matches, key=len))