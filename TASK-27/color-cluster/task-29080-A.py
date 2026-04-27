from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'..\files\27_A_29080.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '3' and data[0] == 'L':
            target.append(dots[-1])

cluster_1 = [x for x in dots if x[1]>10]
cluster_2 = [x for x in dots if x[1]<10]


min_clust = []
max_clust = []
if len(cluster_1)>len(cluster_2):
    min_clust = cluster_2
    max_clust = cluster_1
if len(cluster_1)<len(cluster_2):
    min_clust = cluster_1
    max_clust = cluster_2
center_min = center(min_clust)
center_max = center(max_clust)
A1 = max(dist(center_min, t) for t in target )*10000
A2 = max(dist(center_max, t) for t in target )*10000
print(A1, A2)
