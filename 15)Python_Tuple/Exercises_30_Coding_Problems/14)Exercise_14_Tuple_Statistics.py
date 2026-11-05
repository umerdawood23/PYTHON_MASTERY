"""Exercise 14: Tuple Statistics
Problem Statement: Write a Python program to calculate the total, highest value, 
and lowest value from a tuple of integers using the built-in sum(), max(), and min() functions.
Purpose: This exercise shows that Python’s built-in aggregate functions work directly on tuples, not just lists.
Being able to derive quick statistics from an immutable sequence without converting it first is a practical time-saver in data processing and reporting tasks.

Given Input: scores = (88, 95, 70, 62, 99, 74, 85)
Expected Output: Sum: 573, Max: 99, and Min: 62"""

scores = (88, 95, 70, 62, 99, 74, 85)
sum = sum(scores)
max = max(scores)
min = min(scores)
print(sum)
print(max)
print(min)
