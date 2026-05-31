A = "Umer" #Global Variable

def myfunc():
    global A
    A = "Good"

myfunc()
print("Umer is " + A)
