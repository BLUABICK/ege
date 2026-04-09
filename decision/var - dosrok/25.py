def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            d|= {i}
            d|= {num//i}
    D = []
    M = 0
    for i in d:
        if i%10==7 and i!=7:
            D.append(i)
    if D:
        M = min(D)
    return M

cnt = 0
for N in range(700000, 10**20):
    G = f(N)
    if G:
        print(N, G)
        cnt+=1
        if cnt==5:
            break