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

"""REMOVE()_METHOD"""
REMOVE_METHOD = ["Lora", "MALL", "BC"]
REMOVE_METHOD.remove("BC")
print(REMOVE_METHOD)

"""SORTING_METHOD"""
# Defining Function
def myFunc(e):
	return e.lower()

SORTING_CARS = ["honda", "tesla", "BMW", "volvo"]
SORTING_CARS.sort(reverse = True, key = myFunc)

print(SORTING_CARS)


def myFunc(l):
	return l['year']

SORTING_CARS1 = [
	{'car' : 'Honda' , 'year' : '2000'},
	{'car' : 'Toyota', 'year' : '2005'},
	{'car' : 'City', 'year' : '2010'}
]

SORTING_CARS1.sort(reverse = False, key = myFunc)
print(SORTING_CARS1)

"""Creating a List"""
colors = ["red", "green", "blue"]


"""Print the first item"""
print(colors[0])

"""Change the second itemn to Yellow"""
colors[1] = "yellow"

"""Adding the Purple"""
colors.append("Purple")

"""Remove the Red Color"""
colors.remove("red")

"""Print the List"""
print(colors)