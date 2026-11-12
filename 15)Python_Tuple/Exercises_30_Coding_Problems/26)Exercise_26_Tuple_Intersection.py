"""Exercise 26: Tuple Intersection
Problem Statement: Write a Python program to find all elements that are common to two different tuples.
Purpose: This exercise introduces set intersection as a tool for comparing collections. Finding shared elements between two sequences is a core operation in data analysis, 
deduplication, access control (shared permissions), and any scenario where you need to identify overlap between datasets.

Given Input: t1 = (1, 2, 3, 4, 5, 6) and t2 = (4, 5, 6, 7, 8, 9)
Expected Output: Common elements: (4, 5, 6)
"""

t1 = (1, 2, 3, 4, 5, 6) 
t2 = (4, 5, 6, 7, 8, 9)


common_ordered = tuple(x for x in t1 if x in t2)
print("Common elements (ordered):", common_ordered)