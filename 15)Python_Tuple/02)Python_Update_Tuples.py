#Can add items by converting the tuple to the list

thistuple = ("XAUUSD", "GBPUSD", "EURUSD", "EURJPY")
X = list(thistuple) # Converting the tuple to the list
X[0] = "SPX"
thistuple = tuple(X) # Converting back to the tuple
print(thistuple)

# Using the append Method
Y = list(thistuple)
Y.append("OIL")
thistuple = tuple(Y)
print(thistuple)

# Adding the tuple to the tuple
thistuple_1 = ("SP500", "NASDAQ")
thistuple += thistuple_1
singlitemlist = ("US30", )
thistuple += singlitemlist
print(thistuple)