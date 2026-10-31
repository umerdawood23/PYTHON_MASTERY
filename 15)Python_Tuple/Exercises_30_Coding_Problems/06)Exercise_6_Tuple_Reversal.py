"""Exercise 6: Tuple Reversal
Problem Statement: Write a Python program to reverse the order of elements in a tuple.

Purpose: This exercise shows how to reverse a tuple even though tuples have no built-in .reverse() method (unlike lists).
You will practice using slice notation with a step value, which is a widely used Python idiom for reversing any sequence.

Given Input: items = (1, 2, 3, 4, 5)
Expected Output: (5, 4, 3, 2, 1)"""

items = (1, 2, 3, 4, 5)
items_1 = items[::-1]
print(items_1)
items_2 = reversed(items)
print(items_2)