# Scikit-learn Model Workflow
try:
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit([[1],[2],[3],[4],[5]], [35,45,55,65,75])
    print("Prediction:", round(model.predict([[6]])[0],2))
except ImportError:
    print("Install scikit-learn: pip install scikit-learn")
