# Anomaly Detection Demo
values = [42,44,41,43,45,120,40,42]
mean = sum(values)/len(values)
std = (sum((x-mean)**2 for x in values)/len(values))**0.5
anomalies = [x for x in values if abs(x-mean) > 2*std]
print("Mean:", round(mean,2), "Std:", round(std,2))
print("Anomalies:", anomalies)
