"""Exercise 31: NamedTuples
Problem Statement: Use collections.namedtuple to define an Employee data structure with named fields, create a few instances,
and perform a calculation such as finding the highest-paid employee.
Purpose: This exercise introduces namedtuple as a lightweight way to create readable, self-documenting data objects without the overhead of a full class.
Named tuples are used extensively in standard library code, data pipelines, and anywhere structured records need to be passed around efficiently.

Given Input: Three employees – ("Alice", "Engineering", 95000), ("Bob", "Marketing", 72000), ("Charlie", "Engineering", 88000)"""
from collections import namedtuple

Employee = namedtuple("Employee", ["name","department","salary"])

employees = (
    Employee("Alice", "Engineering", 95000),
    Employee("Bob", "Marketing", 72000),
    Employee("Charlie", "Engineering", 88000),
)

for emp in employees:
    print(f"{emp.name} works in {emp.department} and earns ${emp.salary:,}")

print("----------------------------------------------------------------------")

top = max(employees, key=lambda e: e.salary)
print(f"The Highest paid salary is by: {top.name} (${top.salary:,})")