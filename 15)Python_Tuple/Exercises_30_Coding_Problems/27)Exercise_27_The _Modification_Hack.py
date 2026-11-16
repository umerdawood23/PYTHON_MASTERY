"""Exercise 27: The “Modification” Hack
Problem Statement: Write a Python program to “modify” a tuple by converting it to a list, changing a specific item, and converting it back to a tuple.
Purpose: This exercise highlights the immutability of tuples and demonstrates the standard workaround used when a one-off change is needed. 
Understanding this pattern also helps you appreciate why tuples are immutable by design and when to choose a list instead.
Given Input: colours = ("red", "green", "blue"), replace "green" with "yellow".
"""

colours = ("red", "green", "blue")
list_1 = list(colours)
list_1[1] = "yellow"
list_1 = tuple(colours)
print(list_1)
print(type(list_1))