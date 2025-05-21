
with open('26_3088.txt') as file:
    N = int(file.readline())
    orders = []
    for i in file:
        orders.append(list(map(int, i.split())))

orders.sort(key=lambda x: (x[1], x[0]))
print(orders)

order_cnt= [0] * 1001
order_time = [0] *1001
cr_arf = []
for i in range(0, N-1, 2):
    order_cnt[orders[i][1]] += 1
    print(orders[i][1],orders[i+1][1])
    print(orders[i+1][0], orders[i][0], orders[i+1][0] - orders[i][0])
    order_time[orders[i][1]] += orders[i+1][0] - orders[i][0]
print(order_cnt)
print(order_time)



