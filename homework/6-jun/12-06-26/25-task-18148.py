def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            d |= {i, num//i}
    d_46 = []

    for i in sorted(d):
        if i%100==46:
            d_46 += [i]
    if d_46:
        return d_46[-1]+d_46[0]
    return 0
cnt = 0
for i in range(900001, 10**10):
    M = f(i)
    if M:
        print(i, M)
        cnt+=1
        if cnt==5:
            break