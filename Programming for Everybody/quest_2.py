file_name = input("Enter the file name:")
file_handle = open(file_name, 'r') # assigning handle and opening up the file

count = 0
total = 0.0
Max = 0 

for line in file_handle:
    if not line.startswith("X-DSPAM-Probability:"):
        continue

    #Finding the colon position
    colon_pos = line.find(":")

    #Extracting the values
    value = float(file_handle[colon_pos+1:].strip())

    #Counting all the values
    count = count + 1

    #finding the total
    total = total + value






