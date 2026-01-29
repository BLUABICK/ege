def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    d_8 = []

    for i in sorted(d):
        if i != 8 and i % 10 == 8:
            d_8 += [i]
    if d_8:
        return min(d_8)
    return 0

cnt = 0
for N in range(500_001, 10 ** 20):
    F = f(N)
    if F:
        print(N, F)
        cnt += 1
        if cnt == 5:
            break
