#Write a Python method that reads bytes from a specific range from a file. Range
#min and max values are sent as input parameters

import sys
import os

f_path = os.path.dirname(sys.argv[0])+'/l11.txt'

def read_bites(p1,p2):
    with open(f_path, "rb") as f:
        f.seek(p1-1)
        return f.read(p2-p1)

#generate data
with open(f_path, "wb") as f:
    f.write(b'123456789abcdef')

print(str(read_bites(5,10)))
