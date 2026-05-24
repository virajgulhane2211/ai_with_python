# Artificial Neuron Calculator
inputs = [1,0,1]; weights = [0.7,0.2,0.5]; bias = -0.6
z = sum(i*w for i,w in zip(inputs, weights)) + bias
print("Weighted sum:", round(z,3))
print("Output:", 1 if z >= 0 else 0)
