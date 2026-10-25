"""Exercise 4: Tuple Concatenation
Problem Statement: Write a Python program to join three separate tuples into one new tuple using the + operator.

Purpose: This exercise demonstrates how to combine multiple tuples without modifying any of the originals. Concatenation is useful when you need to assemble a final ordered collection from several independent parts.

Given Input: a = (1, 2), b = (3, 4), and c = (5, 6)

Expected Output: (1, 2, 3, 4, 5, 6)"""


"""chose = 0
while chose < 1: 
    chose = input("chose from the given options:"
    "              Press Yes to continue adding the Numbers." \
    "              Press 0 to stop" \
    "")
if chose == 1:
    try: 
        input_values = input("Enter the tuple values separated by dots: ")
    except TypeError:
        ("Please enter only numbers!")
    except ValueError:
        ("Invalid value!")

    Lora = tuple(y.split() for y in input_values.split('.'))"""


tuple_1 = (1,2)
tuple_2 = (3,4)
tuple_3 = (5,6)

tuple_4 = tuple_1 + tuple_2 + tuple_3
print(tuple_4)