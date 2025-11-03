from re import *

# with open('24-334.txt') as file:
#     text = file.readline()
# pattern = r'[1-9AB][0-9AB]*[02468A]|[02468A]'
#
# matches = [match.group() for match in finditer(pattern, text)]
# print(len(max(matches, key=len)))

with open('Tasks-files/24-347.txt') as file:
    text = file.readline()
pattern = r'[1-7][0-7]*'

matches = [match.group() for match in finditer(pattern, text)]

ans = []
ans1 = []
for i in matches:
    if int(i, 8) % 13 == 0:
        ans.append(i)
    else:
        for j in range(0, len(i)):
            for k in range(1, len(i) - j):
                i_slice = i[j:-k]
                if int(i_slice, 8) % 13 == 0:
                    ans.append(i_slice)
                    break
max_len = []
max_len1 = len(max(ans, key=len))
for i in ans:
    if len(i) == max_len1:
        max_len.append(i)

minn = []
for i in max_len:
    i1 = int(i)
    minn.append(i1)
minn2 = min(minn, key=int)
print(minn2)

print(text.find(str(minn2)))
