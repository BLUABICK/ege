from re import *

# with open('24-337.txt') as file:
#     text = str(file.readline())
#
# pattern = r'[1-9ABCD][0-9ABCD]+'
#
# matches = [match.group() for match in finditer(pattern, text)]
#
# need = []
# need2 = []
#
# for i in matches:
#     if int(i, 14) % 98 == 0:
#         need2.append(i)
#     else:
#         for l in range(0, len(i)):
#             for r in range(1, len(i) - l):
#                 i2 = i[l:-r].lstrip('0')
#                 if i2 and int(i2, 14) % 98 == 0:
#                     need2.append(i2)
# print(need2)
# print(len(max(need2, key=len)))

with open('24-314.txt') as file:
    text = str(file.readline())

must_1 = r'([1-7][0-7]*|0)'
pattern = fr'(?<=F)({must_1}[+*])+{must_1}'
matches = [match.group() for match in finditer(pattern, text)]
max_len = len(max(matches, key=len))

dlin = []
for i in matches:
    if len(i) == max_len:
        dlin.append(i)

maxx2 = max(dlin)
print(maxx2)

maxx3 = ''
i2 = ''
for i in maxx2:
    if i not in '+*':
        i2 += i

    else:
        maxx3 = maxx3 + str(int(i2, 8)) + i
        i2 = ''
print(eval(maxx3+i2))

