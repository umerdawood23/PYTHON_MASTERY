"""Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product; 
otherwise, return their sum."""

# Wrap the input() in int() to convert the string to an integer
Number_One = int(input("Enter the first Number: "))
Number_Two = int(input("Enter the second Number: "))

def product_sum(Number_One, Number_Two):
    product = Number_One * Number_Two

    if product <= 1000:
        return product
    else:
        return Number_One + Number_Two
         
# Call the function once and print it
result = product_sum(Number_One, Number_Two)
print("The result is", result)