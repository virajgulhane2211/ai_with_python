# ANN Forward Propagation
def relu(x): return max(0,x)
x1, x2 = 0.8, 0.4
h1 = relu(0.6*x1 + 0.3*x2 + 0.1)
h2 = relu(0.2*x1 + 0.8*x2 + 0.1)
out = 0.5*h1 + 0.5*h2
print("h1:", round(h1,3), "h2:", round(h2,3), "output:", round(out,3))
