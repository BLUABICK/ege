def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num%i==0:
            if is_prime(i):
                d |= {i}
            if is_prime(num//i):
                d |= {num//i}
    M = 0
    if len(d)>1:
        M = min(d) + max(d)
    if M%100==63 and M%len(d)==0:
        return M
    return 0

cnt = 0
for i in range(7_800_000, 10**20):
    G = f(i)
    if G:
        print(i, G)
        cnt +=1
        if cnt==5:
            break
