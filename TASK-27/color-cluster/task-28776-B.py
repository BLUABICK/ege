from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'../files/27_B_28766.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:].strip() == 'I':
            target.append(list(map(float, [x, y])))

cluster_1 = [x for x in dots if x[1] > 23]
cluster_2 = [x for x in dots if 15 < x[1] < 23]
cluster_3 = [x for x in dots if x[1] < 15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

trg_clust_1 = [x for x in target if x[1] > 23]
trg_clust_2 = [x for x in target if 15 < x[1] < 23]
trg_clust_3 = [x for x in target if x[1] < 15]

dist_trg_1 = min(dist(x, y) for x in trg_clust_1 for y in trg_clust_1 if x != y)
if len(trg_clust_1[1]) > 3:
    dist_trg_2 = min(dist(x, y) for x in trg_clust_2 for y in trg_clust_2 if x != y)
else:
    dist_trg_2 = 10**10
dist_trg_3 = min(dist(x, y) for x in trg_clust_3 for y in trg_clust_3 if x != y)
min_dist_trg = min(dist_trg_1, dist_trg_2, dist_trg_3)

min_trg = min(trg_clust_1, trg_clust_2, trg_clust_3, key=len)
max_trg = max(trg_clust_1, trg_clust_2, trg_clust_3, key=len)

print(len(trg_clust_1), len(trg_clust_2), len(trg_clust_3))

print(min_dist_trg * 10000)
print(dist(center_2, center_3)*10000)