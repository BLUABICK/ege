from re import *
with open(r'../files/24_17641.txt') as file:
    data = file.readline()
num = r'(0|([1-9][0-9]*))'
prods = fr'({num}\*)*0(\*{num})*'
pattern = fr'{prods}(\+{prods})+'

matches = [match.group() for match in finditer(pattern, data)]