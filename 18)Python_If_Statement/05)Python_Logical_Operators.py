"""Python Logical Operators
Logical operators are used to combine conditional statements.
Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
The and Operator
The and keyword is a logical operator, and is used to combine conditional statements. 
Both conditions must be true for the entire expression to be true."""


"""Test if a is greater than b, AND if c is greater than a:"""

a = 200
b = 10
c = 2222

if a > b and c > a:
    print("Both conditions are true!")