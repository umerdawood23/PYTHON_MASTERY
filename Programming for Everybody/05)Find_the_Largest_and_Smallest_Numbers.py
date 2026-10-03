largest = None
smallest = None

while True:
    num = input("Enter the Number: ")


    if num == "done":
        break
    try:
        ivalue = int(num)
    except:
        print("Invalid Input")
        continue

    if largest is None or ivalue > largest:
        largest = ivalue

    if smallest is None or ivalue < smallest:
        smallest = ivalue
print("Maximum is", largest)
print("Smallest is", smallest)