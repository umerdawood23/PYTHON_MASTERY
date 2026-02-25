import pandas as pd
from datetime import datetime

prices_list = [65000, 65100, 65200, 64900, 64800]
timestamps_list = pd.date_range(start="2026-01-01", periods=5, freq="H")

df = pd.DataFrame(data={'Price': prices_list}, index = timestamps_list)
print("Data Frame: ", df)



