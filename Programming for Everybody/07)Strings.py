greet = "Hello"

"""UpperCase"""
Love = greet.upper()
print(Love)


"""LowerCase Letters"""
Love_1 = greet.lower()
print(Love_1)

"""In Operator"""
str = "X-DSPAM-Confidence:  0.8475"

print(str)

num = str.find(":")
print(num)
num_1 = str[num+1:].strip()
print(num_1)
print(float(num_1))

