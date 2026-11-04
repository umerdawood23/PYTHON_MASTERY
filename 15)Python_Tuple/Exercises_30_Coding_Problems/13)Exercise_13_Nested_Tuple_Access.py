"""Exercise 13: Nested Tuple Access
Problem Statement: Write a Python program to access a specific element that is stored inside a tuple which is itself nested inside another tuple.
Purpose: This exercise builds your understanding of nested data structures. Tuples can contain other tuples as elements, and chaining index operators is the standard way to drill down into them.
This pattern appears frequently when working with coordinate grids, database records, and configuration structures.

Given Input: matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

Expected Output: 6
"""

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
num = matrix[0][0]
print(num)