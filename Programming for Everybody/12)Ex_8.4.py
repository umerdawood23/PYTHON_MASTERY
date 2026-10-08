fname = input("Enter the file name: ")
fn = open(fname)            #fn is the file handle

lst = list()                #Iniliating the list

for line in fn:
    words = line.split()

for word in words:
    if word not in lst:
        lst.append(words)

lst.sort()
print(lst)
