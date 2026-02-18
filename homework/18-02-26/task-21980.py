def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}
    d_7=[]
    for i in sorted(d):
        if i != 7 and i % 10 == 7:
            d_7 += [i]
    F = 0
    if len(d_7)>1:
        F = int((sum(d_7)/len(d_7)))
    if F!=0 and F%111==0:
        return F
    return 0


cnt = 0
for N in range(750_000, 0, -1):
    M = f(N)
    if M:
        print(N, M)
        cnt+=1
        if cnt == 5:
            break