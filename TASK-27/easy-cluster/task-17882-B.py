from math import *

def center(cluster):
    res = []
    for dot_1 in cluster:
        sum_dist = sum(dist(dot_1, dot_2) for dot_2 in cluster)
        res.append([sum_dist, dot_1])
    return min(res)[1]
with open(r'../files/27_B_17882.txt') as file:
    dots = [list(map(float, i.split())) for i in file]


cluster_1 = [i for i in dots if i[1]<3]
cluster_2 = [i for i in dots if 3<i[1]<7]
cluster_3 = [i for i in dots if i[1]>7]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print((center_1[0]+center_2[0])/2*10000)
print((center_1[1]+center_2[1])/2*10000)
print((center_1[1]+center_2[1])/2*10000)