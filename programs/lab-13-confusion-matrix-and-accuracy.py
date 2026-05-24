# Confusion Matrix and Accuracy
tp, tn, fp, fn = 40, 45, 5, 10
total = tp + tn + fp + fn
print("Accuracy:", round((tp+tn)/total,3))
print("Precision:", round(tp/(tp+fp),3))
print("Recall:", round(tp/(tp+fn),3))
