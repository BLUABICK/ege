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
    if d:
        M = min(d)+max(d)
        return str(M)
    return 0
cnt = 0
for i in range(5_400_000, 10**10):
    if int(f(i))>60_000 and f(i)==f(i)[::-1]:
        print(i, f(i))
        cnt+=1
        if cnt==5:
            break
