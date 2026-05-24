# K-Means Clustering
from math import dist
points = [(1,2),(2,1),(2,3),(8,8),(9,8),(8,9)]
centroids = [(1,2),(8,8)]
for step in range(3):
    groups = {0:[], 1:[]}
    for p in points:
        i = min(range(2), key=lambda c: dist(p, centroids[c]))
        groups[i].append(p)
    centroids = [(sum(x for x,y in g)/len(g), sum(y for x,y in g)/len(g)) for g in groups.values()]
    print("Step", step+1, groups, centroids)
