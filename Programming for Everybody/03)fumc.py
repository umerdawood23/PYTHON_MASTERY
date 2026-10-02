def computepay(h, r):
    if h <= 40:
        p = h * r
    elif h > 40:
        p = 40 * r + (h - 40) * 1.5
    return computepay 
try:
    h = input("Enter Hours:")
    r = input("Enter rate per hour:")
except TypeError:
    print("Enter the numbers only!")
except ValueError:
    print("Enter the appropriate Number!")
    
p = computepay(10, 20)
print("Pay", p)