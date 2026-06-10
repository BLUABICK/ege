from math import *

with open(r'27_B_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[1] in '89':
            target.append(list(map(float, [x, y])))
print(target)
cluster_1 = [x for x in dots if x[1]>22]
cluster_2 = [x for x in dots if 15<x[1]<22]
cluster_3 = [x for x in dots if x[1]<15]

target_1 = [x for x in target if x[1]>22]
target_2 = [x for x in target if 15<x[1]<22]
target_3 = [x for x in target if x[1]<15]

trg_12 = min(dist(t1, t2) for t1 in target_1 for t2 in target_2)
trg_13 = min(dist(t1, t3) for t1 in target_1 for t3 in target_3)
trg_23 = min(dist(t3, t2) for t3 in target_3 for t2 in target_2)
B1 = min(trg_13, trg_12, trg_23)*10000

tr_1 = [dist(t1, t2) for t1 in target_1 for t2 in target_1 if t1!=t2]+ [dist(t1, t2) for t1 in target_2 for t2 in target_2 if t1!=t2]+ [dist(t1, t2) for t1 in target_3 for t2 in target_3 if t1!=t2]
B2 = sum(tr_1)/len(tr_1)*10000
print(B1, B2)