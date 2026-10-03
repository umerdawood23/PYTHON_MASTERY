num = 0
sum = 0.0

while True:
    value = input("Enter the Number: ")
    if value == "done":
        break
    try:
        value_1 = float(value)
    except:
        print("Invalid Error")
        continue

    num = num + 1 
    sum = sum + value_1

print(num, sum, sum/num)





