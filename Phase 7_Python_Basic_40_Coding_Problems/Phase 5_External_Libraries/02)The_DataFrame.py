import pandas as pd

data = {"Price" : [45000, 46000, 45500], "Volume": [120, 150, 110]}
df = pd.DataFrame(data)

mean_price = df["Price"].mean()

print("Full Data Frame: ", df )
print("The average price: ", mean_price)




