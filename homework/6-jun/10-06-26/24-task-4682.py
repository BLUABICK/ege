from re import *
with open('24_4682.txt') as file:
    data = file.readline()

pattern = r'([AE][DCB])+'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len))//2)