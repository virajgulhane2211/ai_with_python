# Hierarchical Clustering
clusters = [[1],[2],[8],[9]]
def d(a,b): return abs(sum(a)/len(a) - sum(b)/len(b))
while len(clusters) > 1:
    pair = min(((i,j) for i in range(len(clusters)) for j in range(i+1,len(clusters))), key=lambda p: d(clusters[p[0]], clusters[p[1]]))
    i,j = pair; merged = clusters[i] + clusters[j]
    print("Merge", clusters[i], clusters[j])
    clusters = [c for n,c in enumerate(clusters) if n not in pair] + [merged]
