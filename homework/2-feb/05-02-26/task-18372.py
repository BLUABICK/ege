def f(num):
    d = {1}
    for i in range(2, int(num ** .5) + 1):
        if num %i == 0:
            d |={i, num//i}
    A = sum(d)//len(d)
    if A%100==12:
        return A
    return 0

cnt =0

for N in range(770_000 - 1, 0, -1):
    if M:=f(N):
        if M:
            print(N,M)
            cnt+=1
            if cnt == 5:
                break