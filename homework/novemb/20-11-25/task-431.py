def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans =[]
for x in range(100):
    N = 3*7**(x+1)+13*7**(x+2)+31*7**(3*x)+7**(2*x)
    if sum(map(int, convert(N,7)))==18:
        ans.append(x)
print(min(ans))