ans = []
ans_2 = []
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

mr =1000000
for N in range(10, 100):
    R = convert(N, 3)
    if N%2==0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int, R)), 3)
    B = int(R, 3)
    if B <mr:
        mr, mn = B, N
print(mn, mr)
