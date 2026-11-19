"""Exercise 29: Nested Tuple Flattening
Problem Statement: Write a recursive Python function to flatten a deeply nested tuple of tuples into a single flat tuple containing all the individual values.
Purpose: This exercise strengthens your understanding of recursion and type checking. Flattening nested structures is a practical requirement when processing 
tree-shaped data, parsed expressions, or hierarchical configurations where depth is not known in advance.

Given Input: nested = (1, (2, 3), (4, (5, (6, 7))))
Expected Output: Flattened: (1, 2, 3, 4, 5, 6, 7)"""


def flattern(t):
    for item in t:
        if isinstance(item, tuple):
            yield from flattern(item)
        else:
            yield item
            
nested = (1, (2, 3), (4, (5, (6, 7))))
result = tuple(flattern(nested))
print(result)
print(type(result))

