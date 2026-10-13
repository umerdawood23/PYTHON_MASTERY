"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

fname = input("Enter the file name: ")
handle = open(fname)

dict_1 = dict()
for line in handle:
    word = line.split()
    counts = word.find('m')
    w = handle[counts:]
    for count in handle:
        dict_1[count] = dict_1.get(w, 0) + 1

Maxnumber = None
Maxemail = None
for num, email in dict_1:
    if Maxnumber is None or email > Maxemail:
        Maxnumber = num
        Maxemail = email

print(Maxemail, Maxnumber)