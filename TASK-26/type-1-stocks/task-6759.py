with open('../files/26_6759.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file.readlines()]

goods_1 = sorted(goods, reverse=True)
goods_1 = goods_1[N//3:]

goods_2 = sorted(goods, reverse=True)

summ_goods = sum(goods)
for i in range(2, len(goods_2), 3):
    summ_goods-=goods_2[i]

print(sum(goods_1), summ_goods)