#Write a Python program that reads file content and 
# displays the number of lines that were read

import sys
import os

with open(os.path.dirname(sys.argv[0])+'/l9.txt') as f:
    n = 0
    for ln in f:
        n += 1
        print(ln, end ="")

print("\n\nNumber of lines: ", n)
