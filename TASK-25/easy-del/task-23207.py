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
    if len(d)==2 and d[0]*d[1]==num:
        if str(d[0]).count('5') == str(d[1]). count('5')==1:
            return max(d)
    return 0

cnt = 0
for N in range(1_324_728, 10**20):
    M = f(N)
    if M:
        print(N, M)
        cnt+=1
        if cnt == 5:
            break