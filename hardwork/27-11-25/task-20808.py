def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans =[]
for x in range(1, 2031):
    y=7**170+7**100-x
    ans.append([convert(y,7).count('0'),x])
print(max(ans))