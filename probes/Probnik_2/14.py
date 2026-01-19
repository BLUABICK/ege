from string import printable as alph
def convert_2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

ans = []
for x in range(10, 70001):
    y = 5**2025 + 5**400 - x
    y = convert_2(y, 5)
    ans.append([y.count('4'), x])
print(max(ans))
