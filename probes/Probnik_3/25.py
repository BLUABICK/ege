def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num%i==0 and i!=11 and num//i!=11:
                d |={i}
                d |= {num//i}
    d_11 = [i for i in d if i%100==11]
    if d_11:
        return min(d_11)
    return 0
cnt = 0
for N in range(1_350_050, 10**20+1):
    M = f(N)
    if M:
        print(N, M)
        cnt+=1
        if cnt==5:
            break

