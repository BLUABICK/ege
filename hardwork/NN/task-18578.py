def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1,10000):
    R = convert(N, 4)
    if N%4==0:
        R = '2' + R + '03'
    else:
        R = R + convert(N%4*5, 4)
    R = int(R, 4)
    if R <= 567:
        print(N)