fname = input("Enter the name of the list: ")
fn = open(fname)


lst = list()

for line in fn:
    words = line.split()
for word in words:
    if word not in lst:
        lst.append(word)

lst.sort()
print(lst)