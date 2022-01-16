#Write a Python program to append text into a file and displays the new content

import os

os.unlink("tmp.txt") #remove is it was present

with open("tmp.txt", 'a') as f:
    for i in range(10):
        f.write("Line " + str(i) + "\n")

with open("tmp.txt", 'r') as f:
    for ln in f:
        print(ln, end = '')
