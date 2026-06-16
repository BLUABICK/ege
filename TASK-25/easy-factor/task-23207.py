def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i < int(num ** .5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    if len(d)==2 and str(d[0]).count('5')==1 and str(d[1]).count('5')==1:
        return max(d)
    return 0

cnt= 0
for i in range(1324728, 10**10):
    M = fact(i)
    if M:
        print(i, M)
        cnt+=1
        if cnt==5:
            break