# from math import dist
#
# def center(cluster):
#     res = []
#     for dot in cluster:
#         sum_dist = sum(dist(dot, d) for d in cluster)
#         res.append([sum_dist, dot])
#     return min(res)[1]
#
#
# with open('../files/27.21.A_19715.txt') as file:
#     dots = [list(map(float, i.replace(',', '.').split())) for i in file]
#
# eps = 1
# clusters = []
# while dots:
#     cluster = [dots.pop()]
#     for dot in cluster:
#         for d in dots.copy():
#             if dist(dot, d) < eps:
#                 cluster.append(d)
#                 dots.remove(d)
#     if len(cluster)>30:
#         clusters.append(cluster)
#
# centers = [center(cluster) for cluster in clusters]
# # print([len(cluster) for cluster in clusters])
# # print(centers)
# # print(sum([centers[0][0], centers[1][0]])/2*10000)
# # print(sum([centers[0][1], centers[1][1]])/2*10000)


from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open('../files/27.21.B_19715.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 4
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster)>30:
        clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]
print([len(cluster) for cluster in clusters])
print(centers)
print(abs(sum([centers[0][0], centers[1][0],centers[2][0],centers[3][0]])/4)*10000)
print(abs(sum([centers[0][1], centers[1][1],centers[2][1],centers[3][1]])/4)*10000)