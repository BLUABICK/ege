from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_A_29075.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[2:]== 'III':
            target.append(list(map(float, [x, y])))

cluster_1 = [x for x in dots if x[1]>10]
trg_clust_1 = [x for x in target if x[1]>10]
cluster_2 = [x for x in dots if x[1]<10]
trg_clust_2= [x for x in target if x[1]<10]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
max_clust = []
min_clust = []
if len(trg_clust_1)>len(trg_clust_2):
    min_clust = center_2
    max_clust = center_1
else:
    min_clust = center_1
    max_clust = center_2

print(min_clust[0]*10000, max_clust[1]*10000)


