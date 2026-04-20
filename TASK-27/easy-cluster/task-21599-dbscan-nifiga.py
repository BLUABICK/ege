# from math import dist
#
# def center(cluster):
#     res = []
#     for dot in cluster:
#         sum_dist = sum(dist(dot, d) for d in cluster)
#         res.append([sum_dist, dot])
#     return min(res)[1]
#
# with open(r'.\files\27_A_21599.txt') as file:
#     dots = [list(map(float, i.replace(',', '.').split())) for i in file]
#
# cluster_A_1 = [d for d in dots if d[1] > 0.8 * d[0] - 8]
# cluster_A_2 = [d for d in dots if -7 < d[1] < 0.8 * d[0] - 8]
# cluster_A_3 = [d for d in dots if d[1] < - 7]
#
# center_A_1 = center(cluster_A_1)
# center_A_2 = center(cluster_A_2)
# center_A_3 = center(cluster_A_3)
#
# print((center_A_1[0] + center_A_2[0] + center_A_3[0]) / 3 * 10_000)
# print((center_A_1[1] + center_A_2[1] + center_A_3[1]) / 3 * 10_000)

from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [d for d in dots if d[1] > 0.8 * d[0] - 8]
cluster_A_2 = [d for d in dots if -7 < d[1] < 0.8 * d[0] - 8]
cluster_A_3 = [d for d in dots if d[1] < - 7]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)
center_A_3 = center(cluster_A_3)

print((center_A_1[0] + center_A_2[0] + center_A_3[0]) / 3 * 10_000)
print((center_A_1[1] + center_A_2[1] + center_A_3[1]) / 3 * 10_000)