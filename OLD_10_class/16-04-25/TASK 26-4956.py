with open('26_4956.txt') as file:
    N, M = map(int, file.readline().split())
    cheap = dict()
    exp = dict()
    for i in file:
        price, status = map(int, i.split())
        if price <= M:
            if price in cheap:
                cheap[price][status] += 1
            else:
                cheap[price] = [0, 0]
                cheap[price][status] += 1
        else:
            if price in exp:
                exp[price][status] += 1
            else:
                exp[price] = [0, 0]
                exp[price][status] += 1
popular_cheap = min(cheap)
for product in cheap:
     if cheap[popular_cheap][1] < cheap[product][1]:
         popular_cheap = product
popular_exp = min(exp)
for product in exp:
     if exp[popular_exp][1] < exp[product][1]:
         popular_exp = product

exp_popular_bill = popular_exp * exp[popular_exp][1]
cheap_popular_bill = popular_cheap * cheap[popular_cheap][1]
summ = exp_popular_bill + cheap_popular_bill

exp_bill = exp[popular_exp][0]
cheap_bill = cheap[popular_cheap][0]
summ2 = exp_bill+cheap_bill
print(summ, summ2)

