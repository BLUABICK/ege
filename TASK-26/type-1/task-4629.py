with open('../files/26_4629.txt') as file:
    N= int(file.readline())
    goods = [int(i) for i in file.readlines()]

goods_1 = sorted(goods, reverse=True)
goods_2 = sorted(goods)

price_1 = sum(goods_1[:N//4])*0.5 + sum(goods_1[N//4:])
price_2 = sum(goods_2[:N//4])*0.5 + sum(goods_2[N//4:])
print(price_1, price_2)