from re import *
with open('24_18239.txt') as file:
    data = file.readline()

pattern = r'([-][1-9]+)*'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)
