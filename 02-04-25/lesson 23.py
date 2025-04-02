from timeit import timeit

with open('26_4684.txt') as file:
    N = int(file.readline())
    cost = []
    for i in file.readlines():
        cost.append(int(i))
def ART_M(N, cost):
    sale = N//6
    sale2 = N%6
    cust = bill = sum(cost)
    cost.sort()
    for i in range(sale):
        bill -= cost[i]//2
    cost = cost[sale2:]
    for i in range(sale):
        cust -= cost[i*6]//2
    # print(cust, bill)

print(timeit('ART_M(N,  cost)', globals=globals(), number=100))







