# Perceptron Logic Gate OR
def OR(x1,x2):
    return 1 if x1 + x2 - 0.5 >= 0 else 0
for x1 in [0,1]:
    for x2 in [0,1]:
        print(x1, "OR", x2, "=", OR(x1,x2))
