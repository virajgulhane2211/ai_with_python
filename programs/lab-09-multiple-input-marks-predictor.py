# Multiple Input Marks Predictor
def predict(hours, attendance, assignment):
    return min(100, 10 + 4*hours + 0.5*attendance + 0.3*assignment)
print("Predicted marks:", round(predict(5,82,75),2))
