# Simple Linear Regression
x = [1,2,3,4,5]; y = [35,45,55,65,75]
mx, my = sum(x)/len(x), sum(y)/len(y)
m = sum((x[i]-mx)*(y[i]-my) for i in range(len(x))) / sum((i-mx)**2 for i in x)
c = my - m*mx
print("y =", round(m,2), "x +", round(c,2))
print("Prediction for 6 hours:", round(m*6+c,2))
