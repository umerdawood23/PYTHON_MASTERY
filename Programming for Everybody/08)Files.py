"""open, read, write, close"""


"""The files lives in the secondary memory
-- Will talk to database as well
-- Doing things to the files"""

"""Files consists of lines
-- scanning through files and text"""
"""Set of lines flat text files"""

"""File Processing"""
"""Opening a File"""
"""handle = open(filename, mode)
handle = open('mbox.txt', 'r')"""
fand = open('"C:\Users\RBTG V2\Documents\Data For Trading\Min_Data\2026.7.3AUDCAD_dukascopy_M1_UTC-M1-No Session.csv"', 'r')
fand = fand.read()
count = 0


filename = input("Enter the file name:")
try:
    filename = open(filename)
except:
    print("File cannot be opened: ", filename)
    quit()
count = 0
for line in filename:
    if line.startswith('Suhbjet:') :
        count = count + 1
print('There were', count, 'subject lines in', filename)