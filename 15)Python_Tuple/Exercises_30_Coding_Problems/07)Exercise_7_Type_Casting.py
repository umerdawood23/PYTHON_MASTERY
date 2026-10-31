"""Exercise 7: Type Casting
Problem Statement: Write a Python program to convert a list into a tuple using the tuple() constructor.

Purpose: This exercise demonstrates how to convert between mutable and immutable sequence types.
Converting a list to a tuple is a common pattern when you want to protect data from accidental modification, use it as a dictionary key, or pass it to a function that expects an immutable sequence.

Given Input: my_list = [10, 20, 30, 40, 50]
Expected Output: (10, 20, 30, 40, 50) and <class 'tuple'>"""

my_list = [10, 20, 30, 40, 50]
print(type(my_list))
my_tuple = tuple(my_list)
print(type(my_tuple))