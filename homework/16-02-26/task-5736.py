def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d)>=1:
        if max(d)%7==0:
            return max(d)



cnt = 0
for N in range(10**9+1, 10**20):
    if str(N)==str(N)[::-1]:
        M = f(N)
        if M:
            print(N, M)
            cnt += 1
            if cnt == 5:
                break
