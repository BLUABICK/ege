def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = []
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d += [i]
            if is_prime(num // i): d += [num // i]
    if len(d)>12 and [d[i] for i in range(1, 13)]:
        return max(d)
    return 0

cnt = 0
for N in range(24_517_512, 10**20):
    M = f(N)
    if M:
        print(N, M)
        cnt+=1
        if cnt == 5:
            break