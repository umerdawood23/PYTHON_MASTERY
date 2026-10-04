def computegrade(score):
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
            print("D")
    elif score < 0.6:
            print("F")
    return score


score = 0.0
while True:
    try:
        score = float(input("Enter the grade: "))
        if score > 0.0 and 1.0:
             break
             print(score(computegrade))

    except ValueError:
        print("Enter only numbers")
        continue
    except TypeError:
         print("Enter the correct Type of Number")
         continue

    finally:
         print("Ending")

