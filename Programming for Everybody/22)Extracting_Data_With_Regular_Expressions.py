import re

# Prompt the user for the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"  # Default sample file if input is empty

fh = open(fname)
total_sum = 0
count = 0

# Read through the file line by line
for line in fh:
    # Find all sequences of digits in the line
    numbers = re.findall('[0-9]+', line)
    
    # Loop through each extracted string number, convert to int, and add to total
    for num in numbers:
        total_sum = total_sum + int(num)
        count = count + 1

print("Total count of numbers found:", count)
print("Sum:", total_sum)