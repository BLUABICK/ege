def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num%i==0:
            if i%100==11 and i!=11:
                d |= {i}
            if (num // i) % 100 == 11 and (num // i) != 11:
                d |= {(num // i)}
    return d


cnt = 0
for i in range(1_350_051, 10**20):
    G = f(i)

    if G:
        print(i, G)
        cnt+=1
        if cnt==5:
            break