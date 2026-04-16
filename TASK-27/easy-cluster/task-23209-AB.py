from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'../files/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A1 = [d for d in dots if d[0]<5]
cluster_A2 = [d for d in dots if d[0]>5]

center_A1 = center(cluster_A1)
center_A2 = center(cluster_A2)

print(max(center_A1[0], center_A2[0])*10000)
print(max(center_A1[1], center_A2[1])*10000)

with open(r'../files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


cluster_B1 = [d for d in dots if 12 > d[1] > 3]
cluster_B2 = [d for d in dots if 21 > d[1] > 15]
cluster_B3 = [d for d in dots if 27 > d[1] > 21]

center_B1 = center(cluster_B1)
center_B2 = center(cluster_B2)
center_B3 = center(cluster_B3)
center_b_min = center(min(cluster_B1,cluster_B2, cluster_B3, key=len))
center_b_max = center(max(cluster_B1,cluster_B2, cluster_B3, key=len))

print(abs(center_b_min[0]- center_b_max[0])*10000)
print(abs(center_b_min[1] - center_b_max[1])*10000)
