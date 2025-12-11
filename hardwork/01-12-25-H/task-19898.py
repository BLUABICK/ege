def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 10001):
    y =7**270+7**170+7**70-x
    ans.append([convert(y,7).count('0'), x])
print(max(ans, key=lambda z: (z[0], z[1])))
