import pandas as pd
import numpy as np

X = np.array([2000, 400]) # Price and Volume
W = np.array([2, 8])
b = np.array([1,2,3])

output = np.dot(X, W) + b

print(f"Layer Putput: {output}")