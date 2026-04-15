from math import *

with open(r'27_B_17834.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
def center(cluster):
    res = []
    for dot_1 in cluster:
        sum_dist = sum(dist(dot_1, dot_2) for dot_2 in cluster)
        res.append([sum_dist, dot_1])
    return min(res)[1]

cluster_1 = [dot for dot in dots if dot[0]<2 and dot[1]>0]
cluster_2 = [dot for dot in dots if dot[0]<3 and dot[1]>2]
cluster_3 = [dot for dot in dots if dot[0]>5 and dot[1]>2]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print((center_1[0]+center_2[0]+center_3[0])/3*100)
print((center_1[1]+center_2[1]+center_3[1])/3*100)
