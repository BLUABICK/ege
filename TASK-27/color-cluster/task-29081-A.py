from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'..\files\27_A_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            target.append(dots[-1])

cluster_1 = [[d for d in dots if d[1] > 8],
             [d for d in target if d[1] > 8]]

cluster_2 = [[d for d in dots if d[1] < 8],
             [d for d in target if d[1] < 8]]

clusters = [cluster_1, cluster_2]
centers = [center(c[0]) for c in clusters]
ans = [dist(centers[i], d) for i in range(2) for d in clusters[i][1]]
A1 = min(ans)
A2 = max(ans)
print(A1 * 10_000, A2 * 10_000)