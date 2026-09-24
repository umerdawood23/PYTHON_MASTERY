fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)



fruit = ["nangi","Nudes", "Rand"]
fruit.append("Behen kI Lori")
print(fruit)


"""Clear_Method"""
Student = ["Umer", "Ali", "Usman"]
Student.clear()
print(Student)


"""Copy Method"""
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

Num = ["1", "2", "3", "4"]
y = Num.copy()


"""Count() Method"""
Number = [1,2,3,4,5,5,5]
a = Number.count(5)
print(a)

"""Explanation: The count Method returns the specified value from the list
Syntax: list.count(value). The value can be anything ranging from int, float, string, tuple, list etc"""

"""Extend Method()"""
"""Explanation: The Extend Method adds the specified list of elements (or any iterable) at the end of the list"""

Number1 = [1,2,3,4,5]
Number2 = [6,7,8,9,10]
Number2.extend(Number1)
print(Number2)


"""Index() Method"""

"""The Index Method returns the Index of the element in the List"""
# Example:
# Index = Student.index("Umer")

"""Insert Method"""
Insert_Method = ["SPY", "APPL", "TSLA"]
Insert_Method.insert(0, "XAUUSD")
print(Insert_Method)


"""Pop()_Method"""
Insert_Method.pop(0)
print(Insert_Method)