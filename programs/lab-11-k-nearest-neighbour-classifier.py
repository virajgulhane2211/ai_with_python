# K-Nearest Neighbour Classifier
from math import dist
data = [(150,8,"Apple"),(170,7,"Apple"),(30,4,"Grape"),(25,5,"Grape"),(110,9,"Mango")]
new = (120,8); k = 3
near = sorted(data, key=lambda p: dist((p[0],p[1]), new))[:k]
count = {}
for *_, label in near: count[label] = count.get(label,0) + 1
print("Nearest:", near)
print("Prediction:", max(count, key=count.get))
