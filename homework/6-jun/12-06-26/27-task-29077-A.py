from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_A_29077.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0]=='N' and data[1]=='9' and data[2:]=='I':
            target.append(list(map(float, [x, y])))


cluster_1 = [x for x in dots if x[1]>10]
cluster_2 = [x for x in dots if x[1]<10]

target_1 = [x for x in target if x[1]>10]


center_1 = center(cluster_1)
center_2 = center(cluster_2)

A1 = min(dist(center_1, t) for t in target_1)
A2 = max(dist(center_2, t) for t in target_1)
print(str(A1*10000//1)[:-2], str(A2*10000//1)[:-2])