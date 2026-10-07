file = input("Enter the file name: ")
fh = open(file, 'r')

count = 0
total = 0.0

for line in fh:
    #Counting the total number of lines with total
    total = total + 1 

    if not line.startswith('From '):
        continue
    #Counting the total lines
    count = count + 1

print("Total Lines: ",total)
print("Lines starting with 'From ':", count)



