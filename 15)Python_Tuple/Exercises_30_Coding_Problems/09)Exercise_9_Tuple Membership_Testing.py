"""Exercise 9: Tuple Membership Testing

Problem Statement: Write a Python program to check whether a specific element exists inside a tuple using the in keyword.
Purpose: This exercise introduces membership testing, one of the most readable and expressive features of Python. Checking for the presence of a value in a collection is a task that appears constantly in real-world code, from input validation to search logic.

Given Input: fruits = ("apple", "banana", "cherry", "date")
Expected Output: True and False"""

num = input("Enter the character that you want to find: ")


fruits = ("apple", "banana", "cherry", "date")
for x in fruits:
    if x == num:
        print(f"The requiredcharacter has been found:", x)
        break
    else:
        print("Not Found!")
        break
