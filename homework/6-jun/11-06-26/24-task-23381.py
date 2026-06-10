from re import *
with open('24_23381.txt') as file:
    data = file.readline()

pattern = r'[02468][A-Z]*[02468]'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))