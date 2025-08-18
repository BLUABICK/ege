from re import *
# with open(f'Regexp contest/regexp-practice-1.txt') as file:
#     text = str(file.readlines())
#
# pattern = r'\b([cC][aA][tT])\b'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# with open(f'Regexp contest/regexp-practice-2.txt') as file:
#     text = file.readlines()
# pattern = r'(A|a).+'
# for line in text:
#     if match(pattern, line):
#         print(match(pattern,line).group())


# with open(f'Regexp contest/regexp-practice-3.txt', encoding='utf-8') as file:
#     text = str(file.readlines())
# print(text)
# pattern = r'[0-9]+(\.[0-9]+|[0-9]*)'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)


# with open(f'Regexp contest/regexp-practice-4.txt', encoding='utf-8') as file:
#      text = str(file.readlines())
# print(text)
# pattern = r'([0-9]+)-([0-9]+)-([0-9]+)'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# with open(f'Regexp contest/regexp-practice-5.txt', encoding='utf-8') as file:
#     text = file.read()
# pattern = r'[A-ZА-ЯЁ][a-zа-яё]*\b'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

with open(f'Regexp contest/regexp-practice-6.txt', encoding='utf-8') as file:
     text = str(file.readlines())
print(text)
pattern = r'[A-ZА-ЯЁ]{2}-[0-9]{4}'
matches = [match.group() for match in finditer(pattern, text)]
print(matches)