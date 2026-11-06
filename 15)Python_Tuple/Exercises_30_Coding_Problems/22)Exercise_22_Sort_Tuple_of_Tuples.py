"""Exercise 22: Sort Tuple of Tuples
Problem Statement: Write a Python program to sort a tuple of tuples based on the second item in each nested tuple.
Purpose: This exercise teaches you how to use the key parameter of Python’s sorted() function with a lambda to sort
structured data by a specific field – a technique used constantly when ordering records, rankings, and tabular data.
Given Input: students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))"""

students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))
sorted = tuple(sorted(students, key=lambda x:x[1]))

print(sorted)
