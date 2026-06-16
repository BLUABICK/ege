from math import *
with open('inf_22_10_20_26.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file.readlines()]
goods = sorted(goods)
cheap_goods = [i for i in goods if i<=50]
goods = goods[len(cheap_goods):]

cnt_sale = len(goods)//2
last_good = 0
for i in range(cnt_sale):
    last_good = goods[i]
    goods[i] *= 0.75

summ = sum(cheap_goods) + sum(goods)
print(ceil(summ), last_good)