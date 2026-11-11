"""Exercise 25: Tuple Dictionary Mapping
Problem Statement: Write a Python program to zip two tuples together – one holding keys and the other holding values – to create a dictionary.
Purpose: This exercise demonstrates a common pattern for building dictionaries from paired data sources. Combining zip() with dict() is widely
used when parsing CSV headers, mapping configuration keys to values, and constructing lookup tables from separate lists.

Given Input: keys = ("name", "age", "city") and values = ("Alice", 30, "Pune")
Expected Output: {'name': 'Alice', 'age': 30, 'city': 'Pune'}"""


keys = ("name", "age", "city")
values = ("Alice", 30, "Pune")

mapping = dict(zip(keys, values))
print(mapping)

# Alternative: dictionary comprehension
mapping_comp = {k: v for k, v in zip(keys, values)}
print(mapping_comp)