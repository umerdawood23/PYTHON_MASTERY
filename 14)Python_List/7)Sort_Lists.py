"""Question 1: Descending Sort
You are tracking the high scores of a game. Given the list scores = [45, 92, 12, 78, 55], 
write the code to sort the list numerically from highest to lowest, and then print the list."""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


list_score = [45, 92, 12, 78, 55]
list_score.sort(reverse=True)
print(list_score)