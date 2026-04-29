def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(11, 100000):
    R = convert(N, 3)
    cnt_h = 0
    cnt_o = 0
    for i in R:
        if int(i) % 2 == 0:
            cnt_o += 1
        else:
            cnt_h += 1
    if cnt_o > cnt_h:
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        ans.append(R)
print(min(ans))

