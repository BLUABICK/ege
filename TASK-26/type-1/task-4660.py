with open('../files/26_4660.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file.readlines()]

summ = sum(goods)
goods_1 = sorted(goods, reverse=True)
for i in range(3, len(goods_1), 4):
    price = goods_1[i]*0.5
    summ -= goods_1[i]
    summ += price

price_1 = summ


goods_2 = sorted(goods)
for i in range(N//4):
    goods_2[i] = goods_2[i]*0.5
price_2 = sum(goods_2)
print(price_1, price_2)