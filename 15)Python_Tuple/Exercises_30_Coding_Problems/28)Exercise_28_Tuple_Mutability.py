"""Exercise 28: Tuple Mutability
Problem Statement: Create a tuple that contains a list as one of its elements. Modify the list in place and observe that the tuple’s identity stays the same while its contents appear to change.
Purpose: This exercise uncovers one of Python’s most instructive subtleties: a tuple is immutable in the sense that its references cannot be reassigned, but if a reference points to a mutable object such as a list, 
that object itself can still be changed. Understanding this distinction is essential for writing predictable, bug-free code.
Given Input: t = (1, 2, [3, 4, 5]), append 99 to the inner list"""
t = (1, 2, [3, 4, 5])
print("Before", t)
print("Tuple before:", id(t))

t[2].append(99)

print("After", t)
print("Tuple after:", id(t))
