from timeit import timeit

with open('26_4629.txt') as file:
    N = int(file.readline())
    cost = []
    for i in file.readlines():
        cost.append(int(i))
def ART_M(N,  cost):
    cust = bill = 0
    sale = N//4
    cost.sort()
    summ = summ2 = sum(cost)

    for i in range(sale):
        summ -= cost[-i-1]
        cust += cost[-i-1]
        summ2 -= cost[i]
        bill += cost[i]
    cust = cust//2
    summ += cust

    bill = bill//2
    summ2 += bill


print(timeit('ART_M(N,  cost)', globals=globals(), number=100))

