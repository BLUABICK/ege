from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_B_29076.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0]== 'Y':
            target.append(list(map(float, [x, y])))


cluster_1 = [x for x in dots if x[1]>24]
trg_clust_1 = [x for x in target if x[1]>24]
cluster_2 = [x for x in dots if 15<x[1]<24]
trg_clust_2 = [x for x in target if 15<x[1]<24]
cluster_3 = [x for x in dots if x[1]<15]
trg_clust_3 = [x for x in target if x[1]<15]

# cluster_2 - min
# cluster_3 - max

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

B1 = dist(center_2, center_3)*10000

max_dist_1 = max(dist(center_1, d) for d in trg_clust_1)
max_dist_2 = max(dist(center_2, d) for d in trg_clust_2)
max_dist_3 = max(dist(center_3, d) for d in trg_clust_3)

B2 = max([max_dist_1,max_dist_2,max_dist_3])*10000

print(B1,B2)
