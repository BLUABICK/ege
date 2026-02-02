for N in range(2, 100000):
    cnt = 0
    R = str(N)
    for i in R:
        if int(i) % 2 == 0:
            cnt += int(i)

    cnt_2 = sum(map(int, R[1::2]))
    res = abs(cnt - cnt_2)
    if res == 9:
        print(N)
        break
