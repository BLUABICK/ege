from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_B_29077.txt') as file:
    dots = []
    target1 = []
    target2 = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[1] in '89':
            target1.append(list(map(float, [x, y])))
        if data[1]=='0123':
            target2.append(list(map(float, [x, y])))

cluster_1 = [x for x in dots if x[1]>23]
cluster_2 = [x for x in dots if 15<x[1]<23]
cluster_3 = [x for x in dots if x[1]<15]

print(cluster_2)
print(max(cluster_1, cluster_2, cluster_3, key=len))
print(min(cluster_1, cluster_2, cluster_3, key=len))

trg_22 = [x for x in target2 if 15<x[1]<23]
trg_3 = [x for x in target1 if x[1]<15]

print(len(trg_3), len(trg_22))
