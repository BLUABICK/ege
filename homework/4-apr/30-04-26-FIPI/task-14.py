from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'

x = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
y = convert(x, 36)
cnt = 0
for i in y:
    if int(i, 36)%2==0:
        cnt+=1
print(cnt)