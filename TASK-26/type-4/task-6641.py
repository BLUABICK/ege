with open('../files/26_6641.txt') as file:
    N, cost = map(int, file.readline().split())
    items = [list(map(int, i.replace('W', '1').replace('S', '0').split())) for i in file.readlines()]
items = sorted(items)

cnt_s = 0
summ = 0
bought = []
for item in items:
    if summ + item[0] <= cost:
        summ += item[0]
        bought.append(item)
        if item[1] == 0:
            cnt_s += 1

poss_bought = len(bought)
for cost_1 in bought[::-1]:
    if cost_1[1] == 1:
        for cost2 in items[poss_bought:]:
            poss_bought+=1
            if cost2[1] == 0:
                if summ - cost_1[0] + cost2[0] <= cost:
                    bought.remove(cost_1)
                    bought.append(cost2)
                    cnt_s+=1
                    summ+= -cost_1[0] + cost2[0]
                    break

print(cnt_s, cost-summ)
