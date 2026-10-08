"""Total and average value"""

count = 0
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
print(average)    