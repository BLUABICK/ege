from re import *

# with open('Tasks-files/24_9845.txt') as file:
#     text = str(file.readline())
#
# pattern = r'([ABC][89])+'
# matches = [match.group() for match in finditer(pattern, text)]
# print(len(max(matches, key=len)))

# with open('Tasks-files/24_7600.txt') as file:
#     text = file.readline()
# pattern = r'[QRS]?([^QRS]+[QRS])+[^QRS]*'
# matches = [match.group() for match in finditer(pattern, text)]
#
# print(len(max(matches, key=len)))

# with open('Tasks-files/24_7624.txt') as file:
#     text = file.readline()
# pattern = r'[XYZ]?([^XYZ]+[XYZ])+[^XYZ]*'
# matches = [match.group() for match in finditer(pattern, text)]
#
# print(len(max(matches, key=len)))

# with open('Tasks-files/24_8510.txt') as file:
#     text = file.readline()
# pattern = r'[NOP]?([^NOP]+[NOP])+[^NOP]*'
# matches = [match.group() for match in finditer(pattern, text)]
#
# print(len(max(matches, key=len)))

# with open('Tasks-files/24_4710.txt') as file:
#     text = file.readline()
# pattern = r'([CDF][AO])+'
# matches = [match.group() for match in finditer(pattern, text)]
#
# print(len(max(matches, key=len))//2)

with open('Tasks-files/24_6636.txt') as file:
    text = file.readline()
pattern = r'([24680][13579])+'
matches = [match.group() for match in finditer(pattern, text)]

print(len(max(matches, key=len))//2)