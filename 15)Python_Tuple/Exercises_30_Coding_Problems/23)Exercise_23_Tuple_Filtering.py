"""Exercise 23: Tuple Filtering
Problem Statement: Write a Python program to filter a tuple and keep only the elements that satisfy a given condition, using both filter() and a list comprehension approach.
Purpose: This exercise demonstrates two idiomatic ways to select a subset of items from a sequence based on a condition.
Filtering is a foundational operation in data processing, validation, and functional-style programming.

Given Input: numbers = (3, 14, 7, 22, 9, 41, 18, 5), keep only values greater than 10
Expected Output: Filtered: (14, 22, 41, 18)"""

numbers = (3, 14, 7, 22, 9, 41, 18, 5)

# Using filter()
filtered_filter = tuple(filter(lambda x: x > 10, numbers))
print("Using filter(): ", filtered_filter)

# Using a generator expression
filtered_comp = tuple(x for x in numbers if x > 10)
print("Using comprehension:", filtered_comp)