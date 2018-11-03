#Python-3 regular expression example. Extract IP v4 adress

import re

print("\n*** Looking for file with cpp extention ***\n") 

paths = [
"/home/user/work/some_file.txt", 
"/var/log/code.cpp",
"/opt.cpp/set/set.a12",
"/optc/set/not_cpp",
"/cpp/set/other.cpp"
] 

for st in paths:
    sc = re.search(r'\w+\.cpp$', st) 
    if sc:
        print(st)
        print("File: ", sc.group())
  

