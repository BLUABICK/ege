from math import *

with open('../files/27_A_29074.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        if data[0] == 'Z':
            target.append(list(map(float, [x, y])))

trg_clust_1 = [x for x in target if x[1]<10]
trg_clust_2 = [x for x in target if x[1]>10]

trg_min = min(len(trg_clust_1), len(trg_clust_2))
trg_max = max(len(trg_clust_1), len(trg_clust_2))

print(trg_min, trg_max)
