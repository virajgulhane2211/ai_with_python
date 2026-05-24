# Train-Test Split and Overfitting
data = list(range(1,11))
train_size = int(len(data)*0.8)
train, test = data[:train_size], data[train_size:]
print("Train data:", train)
print("Test data:", test)
print("Overfitting means good train result but poor new-data result")
