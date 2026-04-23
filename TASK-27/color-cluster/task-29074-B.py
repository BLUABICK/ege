from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open('../files/27_B_29074.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:].strip()=='V':
            target.append(list(map(float, [x, y])))


cluster_1 = [x for x in dots if x[1]>22]
cluster_2 = [x for x in dots if 16<x[1]<22]
cluster_3 = [x for x in dots if x[1]<15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

trg_clust_2 = [x for x in target if 16<x[1]<22]
trg_clust_3 = [x for x in target if x[1]<15]

dist_trg_2 = min(dist(center_2, c) for c in trg_clust_2)
dist_trg_3 = min(dist(center_3, c) for c in trg_clust_3)
B1=min(dist_trg_2,dist_trg_3)*10000

dist_trg_2 = max(dist(center_2, c) for c in trg_clust_2)
dist_trg_3 = max(dist(center_3, c) for c in trg_clust_3)
B2=max(dist_trg_2,dist_trg_3)*10000

print(B1, B2)