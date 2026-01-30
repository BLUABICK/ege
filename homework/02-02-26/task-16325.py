from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
cnt = 0
y = convert2(2*729**2014 + 2*243**2016 - 2*81**2018 + 2*27**2020 - 2*9**2022 - 2024, 27)
for i in y:
    if int(i, 27)>9:
        cnt+=1
print(cnt)