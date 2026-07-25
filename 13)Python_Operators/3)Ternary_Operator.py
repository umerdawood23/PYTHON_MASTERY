"""Assign the values using ternary operator"""
"""ExampleGet your own Python Server
Assign a value to x:

Assign the value "WEEKEND!" if the number is higher than 5, otherwise "Workday":"""
num = 5 
x = "WEEKEND!" if num > 5 else "Workday"
print(num)


"""Instead of Elif:
The ternary operator can be used instead of elif in longer if statements:

Example
Assign:
- "Fri" if num is 5
- "Sat" if num is 6
- "Sun" if num is 7
- otherwise assign "weekday":"""

num = 5
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)