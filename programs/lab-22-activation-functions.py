# Activation Functions
import math
x = -1.5
print("Step:", 1 if x >= 0 else 0)
print("Sigmoid:", round(1/(1+math.exp(-x)),4))
print("ReLU:", max(0,x))
