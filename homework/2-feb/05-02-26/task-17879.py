def f(num):
    d = {1}
    for i in range(2, int(num ** .5) + 1):
        if num %i == 0:
            d |={i, num//i}
    if len(d)>1:
        M = min(d)+max(d)
        if M%10==4:
            return M
        return 0

cnt =0

for N in range(800_001, 10**20):
    if F:=f(N):
        if F:
            print(N,F)
            cnt+=1
            if cnt == 5:
                break