from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_A_29080.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[1]== '3' and data[2:].strip() =='III':
            target.append(list(map(float, [x, y])))

cluster_1 = [x for x in dots if x[1]>10]
cluster_2 = [x for x in dots if x[1]<10]

target_1 = [x for x in target if x[1]>10]
target_2 = [x for x in target if x[1]<10]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
print(len(cluster_1), len(cluster_2))
len_clust_1 = max(dist(center_1, target1) for target1 in target)
print(len_clust_1)
