from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, d) for d in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'27_B_23284.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


cluster_1 = [dot for dot in dots if 20<dot[0]<28]
cluster_2 = [dot for dot in dots if 12<dot[0]<20]
cluster_3 = [dot for dot in dots if 4<dot[0]<12]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)
dist_12 = dist(center_1, center_2)
dist_13 = dist(center_1, center_3)
dist_23 = dist(center_2, center_3)
print(min(dist_12,dist_23,dist_13)*10000)
print(max(dist_12,dist_23,dist_13)*10000)