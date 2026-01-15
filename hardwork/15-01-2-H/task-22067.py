from string import printable as alph


def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]


x = 3 * 17**777 + 15 * 17**250 - 6 * 17**100 + 2
ans = []
y = convert(x, 17)
for i in y:
    if int(i,17)%2==0:
        ans.append(i)
print(len(set(ans)))