def div(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and i % 2:
            res.add(i)
        if x % i == 0 and (x // i) % 2:
            res.add((x // i))
    if len(res) == 3:
        return sorted(res)
    return 0

for N in range(18782, 18823):
    if div(N):
        print(*div(N))