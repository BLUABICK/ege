def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            d |= {i}
            d |= {num // i}
    d_9 = []
    for i in d:
        if i%10==9 and i!=9:
            d_9.append(i)
    if d_9:
        return min(d_9)
    return 0

cnt = 0
for i in range(800001, 10**20):
    M=f(i)
    if M:
        print(i, M)
        cnt+=1
        if cnt==5:
            break