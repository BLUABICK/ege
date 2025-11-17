def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

x = 5*216**3031+4*36**3042-3*6**3053-3064
print(sum(map(int, convert(x, 6))))