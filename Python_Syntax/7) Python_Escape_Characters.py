txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

Text = f"We are \"Legends\" from Pakistan. I am Born in {20+1}."
print(Text)

"""\'	Single Quote"""
txt = 'It\'s alright.'
print(txt) 

"""\\	Backslash"""
txt = "This will insert one \\ (backslash)."
print(txt) 


"""New Line"""
txt = "Hello\nWorld!"
print(txt) 

Text = "I am Umer\nDawood."
print(Text)

"""Return Value"""
txt = "Hello\rWorld!"
print(txt) 

Text = f"This is Will Only Return the value\r{20+12}."
print(Text)


"""Returning the Tab"""
txt = "Hello\tWorld!"
print(txt) 

Age = 24
value = f"This will give a Tab, such as Umer\tDawood. I am {Age}."
print(value)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

Text = "This will return the Backspace, such as Umer \bDawood."
print(Text)


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


Text = "\000\111\224\223"
print(Text)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

Text = "\x20\x10\x23"
print(Text)