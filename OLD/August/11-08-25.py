import re
from re import match

#
# text = '+79950547467'
# pattern = r'(\+?7|8)\d{10}'
# matches = re.match(pattern, text)
# print(matches)


# with open('reg_exp_task_1.txt') as file:
#     text = file.readline()
#
# pattern = r'\d+'
# matches = re.findall(pattern, text)
# print(matches)

#
# with open('reg_exp_task_2.txt') as file:
#     text = file.readline()
#
# pattern = r'-?\d+\.?\d*'
# matches = re.findall(pattern, text)
# print(matches)

# text = 'abbcc'
# pattern = 'a+b{2,}c+'
# matches = re.sub(pattern, 'HELLO', text)
# print(matches)

#
# with open('reg_exp_task_4.txt') as file:
#     text = file.readline()
#
# pattern = r'\w*@.\w+.'
# matches = re.findall(pattern, text)
# print(matches)


# with open('2400.txt') as file:
#     text = file.readline()
# pattern = r'((NPO)+((NPO)|(PNO))+)|((PNO)+((NPO)|(PNO))+)'
# matches = [match.group() for match in re.finditer(pattern, text)]
# print(len(max(matches, key=len))//3)

