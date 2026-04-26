from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_B_29075.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0]== 'J':
            target.append(list(map(float, [x, y])))

cluster_1 = [x for x in dots if x[1]>22]
trg_clust_1 = [x for x in target if x[1]>22]
cluster_2 = [x for x in dots if 15<x[1]<22]
trg_clust_2= [x for x in target if 15<x[1]<22]
cluster_3 = [x for x in dots if x[1]<15]
trg_clust_3= [x for x in target if x[1]<15]

min_dist = 0

dist_12 = min(dist(x1, x2) for x1 in trg_clust_1 for x2 in trg_clust_2)
dist_13 = min(dist(x1, x2) for x1 in trg_clust_1 for x2 in trg_clust_3)
dist_23 = min(dist(x1, x2) for x1 in trg_clust_2 for x2 in trg_clust_3)

B1 = min([dist_12, dist_13, dist_23])*10000

dist_21 = max(dist(x1, x2) for x1 in trg_clust_1 for x2 in trg_clust_2)
dist_31 = max(dist(x1, x2) for x1 in trg_clust_1 for x2 in trg_clust_3)
dist_32 = max(dist(x1, x2) for x1 in trg_clust_2 for x2 in trg_clust_3)

B2 = max([dist_21, dist_31, dist_32])*10000
print(B1, B2)