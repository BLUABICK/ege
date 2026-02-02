def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1,3001):
    y = 4**210+4**110-x
    ans.append([convert(y, 4).count('0'), x])
print(sorted(ans,key=lambda x: (-x[0], x[1])))
