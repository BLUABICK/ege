def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]

    if len(d) == 2 and str(d[0]).count('2') == 1 and str(d[1]).count('2') == 1:
        return max(d)
    return 0
cnt = 0
for i in range(6_651_220, 2**40):
    M = fact(i)
    if M:
         print(i, M)
         cnt+=1
         if cnt==5:
             break