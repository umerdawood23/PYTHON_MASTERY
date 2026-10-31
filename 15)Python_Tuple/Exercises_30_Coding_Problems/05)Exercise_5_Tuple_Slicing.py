"""Problem Statement: Write a Python program to extract a specific portion of a tuple using slice notation.

Purpose: This exercise teaches you how to retrieve a contiguous subset of elements from a tuple without a loop.
Slicing is a fundamental Python skill used across strings, lists, and tuples alike, and it is essential for tasks like pagination, windowing, and data partitioning.

Given Input: numbers = (10, 20, 30, 40, 50, 60, 70)

Expected Output: (30, 40, 50)"""

numbers = (10, 20, 30, 40, 50, 60, 70)
numbers_1 = numbers[2:5]
print(numbers_1)