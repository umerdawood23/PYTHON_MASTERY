"""Exercise 1: Basic Tuple Operations
Problem Statement: Write a Python program to create a tuple, access its elements by index, and find its length.
Given Input: fruits = ("apple", "banana", "cherry", "date")

Expected Output: First element: apple, Last element: date, and Length: 4"""

fruits = ("apple", "banana", "cherry", "date")

first_element = (fruits[0])
last_element = (fruits[-1])
lenght = (len(fruits))
print(f"First element: ",first_element, "Last element: ",last_element, "and Length: ", lenght)