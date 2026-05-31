import pandas as pd
from sklearn.neural_network import MLPRegressor

# 1. Data Science Process: Extracting & Preparing (Interdisciplinary)
# Loading your XAUUSD tick data
data = pd.DataFrame({'price_t_1': [2100, 2105, 2110], 'volume': [300, 450, 600], 'target': [2105, 2110, 2115]})
X = data[['price_t_1', 'volume']]
y = data['target']

# 2. Machine Learning: The algorithm 'learns' from examples
# Using a 'Neural Network' (the engine of Deep Learning)
model = MLPRegressor(hidden_layer_sizes=(5, 5), max_iter=1000)
model.fit(X, y)

# 3. AI Intelligence: Making a prediction without being explicitly programmed
prediction = model.predict([[2115, 700]])
print(f"Neural Network Predicted Next Price: {prediction[0]:.2f}")