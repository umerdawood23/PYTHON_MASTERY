import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Goal: Predict Gold Price (y) based on Volume (x)
# 2. Selection: Loading our 'Big Data' (Simplified here)
df = pd.DataFrame({'vol': [100, 200, 150, 300, 250], 'price': [2100, 2105, 2102, 2110, 2108]})

# 3. Preprocessing: Flagging errors (e.g., negative volume)
df = df[df['vol'] > 0] 

# 4. Transformation: Reshaping for Scikit-Learn
X = df[['vol']]
y = df['price']

# 5. Mining: Applying the Linear Regression algorithm
model = LinearRegression().fit(X, y)

# 6. Evaluation: Checking the 'Score' (Efficiency)
accuracy = model.score(X, y)
print(f"Model Effectiveness: {accuracy * 100:.2f}%")