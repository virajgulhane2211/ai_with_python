# Distance Measures
from math import sqrt
a, b = (2,3), (8,7)
euclidean = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
manhattan = abs(a[0]-b[0]) + abs(a[1]-b[1])
print("Euclidean:", round(euclidean,2))
print("Manhattan:", manhattan)
