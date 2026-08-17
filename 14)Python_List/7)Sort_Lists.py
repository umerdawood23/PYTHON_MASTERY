"""Question 1: Descending Sort
You are tracking the high scores of a game. Given the list scores = [45, 92, 12, 78, 55], 
write the code to sort the list numerically from highest to lowest, and then print the list."""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


list_score = [45, 92, 12, 78, 55]
list_score.sort(reverse=True)
print(list_score)


"""Question 2: Case-Insensitive Sort
You have a list of names entered by users with inconsistent capitalization: 
names = ["Zack", "alice", "Bob", "charlie"]. 
Write the code to sort this list alphabetically while ignoring the case sensitivity, so that "alice" correctly appears before "Bob". 
Print the sorted list."""

names = ["Zack", "alice", "Bob", "charlie"]
names.sort(key = str.lower)
print(names)

"""Question 3: Custom Sort Function
You want to sort a list of numbers based on how close they are to the number 10.
Given the list numbers = [2, 15, 8, 22, 11], write a custom function to calculate the difference from 10, 
and use it as the key to sort the list. Print the sorted list."""


def myfunc(n):
    return abs(n - 10)

list = [2, 15, 8, 22, 11]
list.sort(key = myfunc)
print(list)

"""Question 4: Pure Reversal
You have a list representing a user's browsing history: history = ["home", "about", "contact", "success"]. 
Write the code to reverse the exact order of this list (most recent first) without sorting it alphabetically. Print the reversed list."""

history = ["home", "about", "contact", "success"]
history.sort(reverse = False)
print(history)