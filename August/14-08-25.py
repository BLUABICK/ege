from re import *

# with open('2405.txt') as file:
#     text = file.readline()
#
# pattern = r'((KLMN)?(KLMN)*)|((LMN)?(KLMN)*)|((MN)?(KLMN)*)|((N)?(KLMN)*)'
# matches = [match.group() for match in finditer(pattern, text)]
# print(len(max(matches)))

# with open('2416.txt') as file:
#     text = file.readline()
# pattern = r'([AE][BCD])+'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)
# print(len(max(matches, key=len)) // 2)

with open('Tasks-files/2402.txt') as file:
    text = file.readline()
number = r'([789][0789]*|0)'
pattern = fr'({number}[\*\-])+{number}'
matches = [match.group() for match in finditer(pattern, text)]
print(matches)
print(len(max(matches, key=len)))
