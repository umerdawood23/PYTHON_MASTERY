import numpy as np

# 1. Input Data (Matrix X) - e.g., Price and Volume
X = np.array([2150.5, 500]) 

# 2. Weights (Matrix W) - What the network 'learns'
W = np.array([[0.2, 0.8], 
              [0.5, -0.1], 
              [0.9, 0.4]])

# 3. Bias (b)
b = np.array([0.1, 0.2, 0.3])

# 4. The Transformation (Dot Product + Bias)
# This is what GPUs do tens of thousands of times per second
output = np.dot(W, X) + b

print(f"Layer Output: {output}")