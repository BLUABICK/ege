from re import *
with open('24_17878.txt') as file:
    data = file.readline()

pattern = r'([0]|[6789][06789]*)([-*]([0]|[6789][06789]*))+'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)
print(len(max(matches, key=len)))