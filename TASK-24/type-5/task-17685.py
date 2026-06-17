from re import *
with open(r'../files/24_17685.txt') as file:
    data = file.readline()

num = r'(0|([1-9][0-9]*))'
pattern = fr'{num}([*+]{num})+'

matches = [match.group() for match in finditer(pattern, data)]

ans=0
for match in matches:
    if eval(match)==0:
        ans = max(ans, len(match))
    else:
        len_match = len(match)
        if len_match>ans:
            for l in range(len_match-1):
                if match[l] in '*+':continue
                if match[l]=='0' and match[l+1] not in '*+': continue
                for r in range(len_match-1, l+1, -1):
                    if match[r] in '*+': continue
                    new = match[l:r + 1]
                    if eval(new) == 0:
                        ans = max(ans, len(new))
                        break
print(ans)