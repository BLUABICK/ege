from re import *
with open(r'../files/24_9791.txt') as file:
    data = file.readline()

pattern = r'[1-9A-F][1-9A-F]*'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))