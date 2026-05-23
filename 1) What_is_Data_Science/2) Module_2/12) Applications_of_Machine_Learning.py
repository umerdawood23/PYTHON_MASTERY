from sklearn.naive_bayes import GaussianNB
import numpy as np

# 1. Features (X): [RSI_Value, Volatility_Index]
# 2. Target (y): [0 = No Trade, 1 = Good Trade]
X = np.array([[30, 0.5], [70, 0.8], [45, 0.2], [25, 0.9], [80, 0.1]])
y = np.array([1, 0, 1, 1, 0])

# 3. Training the 'Naive Bayes' Model
model = GaussianNB()
model.fit(X, y)

# 4. Prediction: New Market Data comes in
# RSI is 28 (Oversold), Volatility is 0.6
new_data = [[28, 0.6]]
prediction = model.predict(new_data)

print(f"Trade Recommendation (1=Buy, 0=Wait): {prediction[0]}")