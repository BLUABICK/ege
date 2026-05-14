from re import *
with open(r'../files/24_8510.txt') as file:
    data = file.readline()

pattern = r'[NOP]([^NOP]+[NOP])*'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches,key=len)))