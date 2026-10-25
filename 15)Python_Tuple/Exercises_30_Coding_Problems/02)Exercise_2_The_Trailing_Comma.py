"""Exercise 2: The Trailing Comma
Problem Statement: Write a Python program to create a tuple containing a single item, the number 50, and confirm its type.

Purpose: This exercise highlights one of the most common beginner mistakes with tuples: assuming that parentheses alone create a tuple. A trailing comma is required when the tuple has only one element, and this exercise trains you to remember that rule.

Given Input: A single integer value 50

Expected Output: (50,) and <class 'tuple'>"""

Trailing_Coma = (50)
print(f"Expected Output: ", Trailing_Coma, "and type: ", (type(Trailing_Coma)))