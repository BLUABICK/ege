from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open('27_A_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
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

cluster_1 = clusters[0]

cluster_2 = clusters[1]

max_cluster = []
if len(cluster_1)> len(cluster_2):
    max_cluster=cluster_1
else:
    max_cluster=cluster_2
cnt = 0
for i in max_cluster:
    if i[1]<centers[1][1]:
        cnt+=1
print(centers)
print(cnt, abs(centers[0][0]-centers[1][0])*10000)

print('чего нахер')