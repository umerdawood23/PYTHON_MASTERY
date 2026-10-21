Symbol = ("XAUUSD", "GBPUSD", "EURJPY", "EURUSD", "GBPJPY")

# Unpacking the symbols by giving each value a variable
(GOLD, POUND_USD, EURO_JPY, EURO_USD, POUND_USD) = Symbol
print(GOLD)
print(POUND_USD)
print(EURO_JPY)
print(EURO_USD)
print(POUND_USD)

# Giving asterik (*) to the variables

(GOLD, POUND_USD, *EURO_JPY) = Symbol
print(*EURO_JPY) 

(GOLD, *POUND_USD) = Symbol
print(*POUND_USD)