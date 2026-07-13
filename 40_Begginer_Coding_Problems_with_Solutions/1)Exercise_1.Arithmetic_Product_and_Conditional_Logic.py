"""Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product; 
otherwise, return their sum."""


def calculate_product_or_sum(num1, num2):
    product = num1 * num2
    
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Get input from the user and convert to integers
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))

# Call the function and print the result
result = calculate_product_or_sum(number_one, number_two)
print(f"The result is: {result}")


"""Enter Multiple Values"""
"""You can add multiple inputs in one line in python with the help of Slipt Function"""

name, age, profession = ("Enter your name, age, profession, separated by spaces.").split()
print("\n")


