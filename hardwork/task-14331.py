def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if sum(map(int, R))%3==0:
        R = R + '212'
    else:
        R = R + convert(sum(map(int,R))*2, 3)
    R = int(R,3)
    if R >490:
        ans.append(R)
print(min(ans))