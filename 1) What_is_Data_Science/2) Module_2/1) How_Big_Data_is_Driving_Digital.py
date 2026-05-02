import pandas as pd
import numpy as np

# 1. Structured Data: Comparing Strategy A (Mid-range) vs Strategy B (3-pointer)
# Probability of success vs Reward
strategies = pd.DataFrame({
    'Strategy': ['Mid-Range 2pt', 'Long-Range 3pt', 'Inside Dunk'],
    'Prob_Success': [0.45, 0.36, 0.70], # P(Make)
    'Reward': [2, 3, 2]                # Point Value
})

# 2. Calculating Expected Value (The core of the 'Transformation')
strategies['Expected_Value'] = strategies['Prob_Success'] * strategies['Reward']

# 3. Identify the 'Game Changer'
best_strategy = strategies.loc[strategies['Expected_Value'].idxmax()]

print("Strategy Analysis:")
print(strategies)
print(f"\nTransformational Insight: Focus on {best_strategy['Strategy']}!")

import pandas as pd
import numpy as np

strategies = pd.DataFrame({
    'Strategy':['Mid-Range 2pt', 'Long-Range 3pt', 'Inside Dunlk'],
    'Prob_Sucess':[0.45, 0.44, 0.60],
    'Reward':[2, 5, 3]
})

