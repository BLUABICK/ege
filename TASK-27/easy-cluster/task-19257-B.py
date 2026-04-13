from math import *

with open(r'../files/27_B_19257.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


def centre(cluster):
    res = []
    for dot in cluster:
        sum_dis = sum(dist(dot, dot2) for dot2 in cluster)
        res.append([sum_dis, dot])
    return min(res)[1]


cluster_1 = [i for i in dots if i[0]<0]
cluster_2 = [i for i in dots if i[1]>7]
cluster_3 = [i for i in dots if 0<i[0] and i[1]<7]

center_1 = centre(cluster_1)
center_2 = centre(cluster_2)
center_3 = centre(cluster_3)

print(abs((center_1[0]+center_2[0]+ center_3[0]))/3*10000)
print(abs((center_1[1]+center_2[1]+center_3[1]))/3*10000)
