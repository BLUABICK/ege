from re import *
with open('24 (1).txt') as file:
    text = file.readline()
pattern = r'(([789][0789]*|0)[\*\-])+([789][0789]*|0)'
matches = [match.group() for match in finditer(pattern, text)]
print(len(max(matches, key=len)))
