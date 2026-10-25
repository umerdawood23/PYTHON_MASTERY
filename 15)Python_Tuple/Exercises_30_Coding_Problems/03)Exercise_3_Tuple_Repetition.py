"""Exercise 3: Tuple Repetition
Problem Statement: Write a Python program to repeat a tuple three times using the * operator.

Purpose: This exercise shows how the * operator works with sequences. Repeating a tuple is a concise way to generate patterned data without writing loops, and it reinforces the idea that tuples support sequence operations just like strings and lists.

Given Input: colors = ("red", "green")

Expected Output: ('red', 'green', 'red', 'green', 'red', 'green')"""

colors = ("red", "green")
colors_1 = colors *3
print(colors_1)
