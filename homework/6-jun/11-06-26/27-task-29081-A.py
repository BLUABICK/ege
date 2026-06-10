from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'27_A_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data=='VII' :
            target.append(list(map(float, [x, y])))
print(target)
cluster_1 = [x for x in dots if x[1]>10]
cluster_2 = [x for x in dots if x[1]<10]

target_1 = [x for x in target if x[1]>10]
target_2 = [x for x in target if x[1]<10]
print(target_1)
center_1 = center(cluster_1)
center_2 = center(cluster_2)

min_d_1 = min(dist(center_1, trg) for trg in target_1)
min_d_2 = min(dist(center_2, trg) for trg in target_2)
A1= min(min_d_1, min_d_2)*10000
max_d_1 = max(dist(center_1, trg) for trg in target_1)
max_d_2 = max(dist(center_2, trg) for trg in target_2)
A2= max(max_d_1, max_d_2)*10000
print(A1, A2)