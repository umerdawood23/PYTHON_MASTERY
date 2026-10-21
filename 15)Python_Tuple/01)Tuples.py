thistuple = ("GBPJPY", "EURJPY", "EURUSD", "GBPUSD", "XAUUSD")
print(thistuple)
print(len(thistuple))

# The Indexing in the tuples
print(thistuple[0:5])

#Access Tuple Items
print(thistuple[0:3])

#Negative Indexing
#Negative Indexing refers to the indexing of the Tuple by accessing them by there Index
print(thistuple[-1])

#Range of Indexes
print(thistuple[0:4])
# If first Item not specified then it starts from 0 and goes to the specified item 
print(thistuple[:5])

#If starting value is left out, then it will go to the end.
print(thistuple[2:])

#Negative Indexing, Specifying the value
print(thistuple[-5:-1])