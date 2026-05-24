# Supervised Learning Workflow
data = [(1,35),(2,45),(3,55),(4,65),(5,75),(6,85)]
train, test = data[:4], data[4:]
def predict(hours): return 25 + 10 * hours
print("Train:", train)
for h,actual in test:
    print("hours", h, "actual", actual, "predicted", predict(h))
