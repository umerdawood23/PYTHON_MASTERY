# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0 # This will store the values of counting
total = 0.0 # This will store the sum of values

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Counting the number of lines
    count = count + 1
    # Getting the colon postion
    colon_pos = line.find(':')
    # Now getting the the float values
    value = float(line[colon_pos+1:].strip())
    # Suming up the values
    total = total + value
    
    
Average = total / count
print("Average spam confidence:", float(Average))
