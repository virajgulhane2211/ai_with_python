# Choosing K using Inertia
def inertia(groups):
    total = 0
    for g in groups:
        c = sum(g)/len(g)
        total += sum((x-c)**2 for x in g)
    return total
for k, groups in [(1,[[1,2,3,10,11,12]]),(2,[[1,2,3],[10,11,12]]),(3,[[1,2],[3,10],[11,12]])]:
    print("K", k, "Inertia", round(inertia(groups),2))
