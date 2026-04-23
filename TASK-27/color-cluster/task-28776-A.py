from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'../files/27_A_28766.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0]== 'Y' and data[2:].strip() =='III':
            target.append(list(map(float, [x, y])))


cluster_1 = [x for x in dots if x[1]<8]
cluster_2 = [x for x in dots if x[1]>8]
cluster_min = min(cluster_1,cluster_2, key=len)

center_min= center(cluster_min)

min_dist = []
distance= [dist(i, center_min) for i in target]

print(min(distance)*10000, max(distance)*10000)
