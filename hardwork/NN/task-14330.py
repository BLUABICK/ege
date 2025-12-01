alp = []
for N in range(10000, 100000):
    a_max = max(map(int, str(N)))
    a_min = max(map(int, str(N)))
    sum_a = (a_min+a_max) **2
    d = 1
    for i in str(N):
        if int(i)%2== 0:
            d*=int(i)
    g = [sum_a, d]
    h = int(str(max(g)) + str(min(g)))
    if h == 12116:
        print(N)




