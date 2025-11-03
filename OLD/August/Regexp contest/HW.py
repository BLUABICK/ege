from re import *

# задача 7
# with open(f'regexp-practice-7.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
# pattern = r'\S+@\S+\b'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# задача 8
# with open(f'regexp-practice-8.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
# pattern = r'(\+?7|8)(\(?.+\)?)(.+\-?)(.+\-)\d{2}'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# задача 9
# with open(f'regexp-practice-9.txt', encoding='UTF-8') as file:
#     text = file.read()
# must_1 = r'<a href="'
# must_2 = r'">'
# pattern = fr'(?<={must_1}).+?(?={must_2})'
# # pattern = '((https?://[^"]+))'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# задача 10
# with open(f'regexp-practice-10.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
# pattern = r'\d'
# matches = sub(pattern, '#', text)
# print(matches)

# задача 11
# with open(f'regexp-practice-11.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
# pattern = r'<[^>]+?>'
# matches = sub(pattern, '', text)
# print(matches)

# задача 12 не моё
# with open(f'regexp-practice-12.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
#
# pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
# result = sub(pattern, lambda match: match.group(0).lower(), text)
# print(result)


# задача 13
# with open(f'regexp-practice-13.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
# pattern = r'\b(\w+)(\s+\1)+\b'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# задача 14
# with open(f'regexp-practice-14.txt', encoding='UTF-8') as file:
#     text = str(file.readlines())
# pattern = r'\b([A-ZА-Я][a-zA-Zа-яА-Я]+) ([A-ZА-Я][a-zA-Zа-яА-Я]+) ([A-ZА-Я][a-zA-Zа-яА-Я]+)\b'
# matches = [match.group() for match in finditer(pattern, text)]
# print(matches)

# задача 15
# не ну это уже сумашествие