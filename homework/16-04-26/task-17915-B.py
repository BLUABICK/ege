from math import *

with open(r'27_B_17915.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

def center(cluster):
    res = []
    for dot_1 in cluster:
        sum_dist = sum(dist(dot_1, dot_2) for dot_2 in cluster)
        res.append([sum_dist, dot_1])
    return min(res)[1]

cluster_1 = [dot for dot in dots if dot[1]>16 and dot[0]<12]
cluster_2 = [dot for dot in dots if dot[1]<9 and dot[0]<15]
cluster_3 = [dot for dot in dots if dot[1]<11 and dot[0]>15]
cluster_4 = [dot for dot in dots if dot[1]>15 and dot[0]>23]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)
center_4 = center(cluster_4)

print((center_1[0]+center_2[0]+center_3[0]+center_4[0])/4*10000)
print((center_1[1]+center_2[1]+center_3[1]+center_4[1])/4*10000)