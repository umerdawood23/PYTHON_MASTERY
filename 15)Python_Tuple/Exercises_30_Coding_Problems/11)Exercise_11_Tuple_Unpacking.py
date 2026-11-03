"""Exercise 11: Tuple Unpacking
Problem Statement: Write a Python program to unpack a four-element tuple into four distinct variables in a single assignment.
Purpose: This exercise introduces tuple unpacking, one of Python’s most elegant features. Unpacking makes code more readable by giving meaningful names to positional data, and it is widely used when working with function return values, database rows, and coordinate pairs.

Given Input: person = ("Alice", 30, "Engineer", "Pune")
Expected Output: Name: Alice, Age: 30, Job: Engineer, and City: Pune"""

person = ("Alice", 30, "Engineer", "Pune")
(Name, Age, Job, City) = person
print("Name:", Name, "Age:", Age, "Job:", Job, "and City:", City)
