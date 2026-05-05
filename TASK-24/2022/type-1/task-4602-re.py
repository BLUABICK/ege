from re import *

with open('../files/24_4602.txt') as file:
    data = file.readline()

pattern = r'([BCD][AO])+'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)
print(len(max(matches,key=len))//2)