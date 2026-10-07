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
for lora in fand:
    print(lora)
