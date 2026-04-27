from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'..\files\27_B_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] >= '8':
            target.append(dots[-1])


trg_clust_1 = [x for x in target if x[1]>24]
trg_clust_1_1 = trg_clust_1.copy()
trg_clust_2 = [x for x in target if 15<x[1]<24]
trg_clust_2_1 = trg_clust_2.copy()
trg_clust_3 = [x for x in target if x[1]<15]
trg_clust_3_1 = trg_clust_3.copy()



min_dist_12 = min(dist(t1, t2) for t1 in trg_clust_1 for t2 in trg_clust_2)
min_dist_13 = min(dist(t1, t3) for t1 in trg_clust_1 for t3 in trg_clust_3)
min_dist_23 = min(dist(t2, t3) for t2 in trg_clust_2 for t3 in trg_clust_3)
B1 = min(min_dist_12,min_dist_13,min_dist_23)*10000

dist_1 = [dist(a,b) for a in trg_clust_1 for b in trg_clust_1_1 if a!=b]
dist_2 = [dist(a,b) for a in trg_clust_2 for b in trg_clust_2_1 if a!=b]
dist_3 = [dist(a,b) for a in trg_clust_3 for b in trg_clust_3_1 if a!=b]
d = dist_1+dist_2+dist_3
B2 = sum(d)/len(d)*10000
print(B1, B2)




