try:
    score = float(input("Enter Score: "))
except ValueError:
    print("Enter only the numbers!")
except TypeError:
    print("Enter the correct value")
    
if score < 0.0 or score > 1.0:
    print("Enter correct range")

if score >= 0.9:
    print("Grade A")
elif score >= 0.8:
    print("Grade B")
elif score >= 0.7:
    print("Grade C")
elif score >= 0.6:
    print("Grade D")
else:
    print("Grade F")

print("ENDING")