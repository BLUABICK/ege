def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for x in range(1, 1000):
    for y in range(1,1000):
        c = 5**50+5**30-5**x-y-5**y-x
        c = convert(c, 5)
        if int(c)>0 and c.count('0')==10:
            ans.append(x*y)
print(max(ans))