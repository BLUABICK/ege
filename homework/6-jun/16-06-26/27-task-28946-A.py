from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open('27_A_28946 (1).txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file.readlines()]

cluster_1 = [x for x in dots if x[1]>15]
cluster_2 = [x for x in dots if x[1]<15]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
cnt = 0
for dot in cluster_1:
    if dot[1]<center_1[1]:
       cnt+=1

print(cnt, abs(center_1[0]-center_2[0])*10000//1)

