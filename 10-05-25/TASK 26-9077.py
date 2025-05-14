with open('26_9077.txt') as file:
    M, N = map(int, file.readline().split())
    customers = []
    for i in file:
        customers.append(list(map(int, i.split())))


customers.sort()
print(customers)
cnt =0
cnt2 = 0
parking = dict()
busy = []
for i in range(1, M+1):
    parking[i] = []

for customer in customers:
    if not parking[customer[2]] or min(parking[customer[2]])>=customer[0]:
        cnt+=1
    else:
        parking[customer[2]].remove(min(parking[customer[2]]))
    parking[customer[3]].append(customer[0]+customer[1])

timeline = [0]*10_000

client = dict()
for customer in customers:
    for i in range(customer[0], customer[0]+customer[1]):
        timeline[i] +=1
print(cnt, max(timeline))

