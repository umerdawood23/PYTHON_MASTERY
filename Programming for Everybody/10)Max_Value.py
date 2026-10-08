"""Total and average value"""

"""count = 0
total = 0.0

while True:
    try:
        inp = input("Enter the number: ")
        if inp == 'done': break
    except:
        print("Invalid Input")
        continue

    float_value = float(inp)
    count = count + 1
    total = total + float_value

average = total / count
print(average) """

numlist = list()

while True:
    try:
        inp = input("Enter the numbers: ")
        if inp == 'done': break
    except ZeroDivisionError:
        print("Cannot be divided by zero")
        
    except ValueError:
        print("Incorrect value")
        continue

    
    value = float(inp)
    numlist = numlist.append(value)

average = (sum(numlist)) / (len(numlist))
print("The average of the numbers are: ", average)