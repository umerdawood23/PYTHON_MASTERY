thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

"""Use the list() method"""

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)




"""Use the slice Operator"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


"""there are several ways to join the list."""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


for x in list2:
    list3.append(x)
print(list3)

