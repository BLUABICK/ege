with open('../files/26_17687.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]

goods_1 = sorted(goods, reverse=True)

M= N//9
goods_1 = goods_1[M:]

goods_2 = sorted(goods, reverse=True)

for i in range(8, len(goods_2), 9):
    goods_2[i] *=0
print(sum(goods_1), sum(goods_2))