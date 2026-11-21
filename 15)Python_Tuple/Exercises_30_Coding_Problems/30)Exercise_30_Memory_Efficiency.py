"""Exercise 30: Memory Efficiency

Problem Statement: Use the sys module to measure and compare the memory consumed by a list and a tuple, each holding the same one million integer elements.
Purpose: This exercise gives you concrete, measurable evidence for one of the key practical advantages of tuples over lists: lower memory overhead.
This matters in performance-sensitive applications that hold large collections of fixed data in memory.

Given Input: A range of one million integers, range(1_000_000), stored as both a list and a tuple
Expected Output: Printed byte sizes for the list and the tuple, followed by the difference in bytes (exact values vary by Python version and platform)"""

import sys

list_1 = list(range(1_000_000))
tuple_1 = tuple(range(1_000_000))
print(f'The Size of List is:', sys.getsizeof(list_1))
print(f'The Size of tuple is:', sys.getsizeof(tuple_1))

print(f'The List of command line arguments passed toscript:', sys.argv(list_1))