# NumPy Array Operations
try:
    import numpy as np
    a = np.array([10,20,30,40])
    print("Array:", a)
    print("Mean:", np.mean(a))
    print("Doubled:", a*2)
except ImportError:
    print("Install NumPy: pip install numpy")
