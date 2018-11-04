#Python-3 regular expression example. Extract IP v4 adress
import re

def apply_exp(lst, exp, comment):
    print(comment) 
    for st in lst:
        print(st, end ="\t")
        sc = re.search(exp , st) 
        if sc:
            print("File: ", sc.group())
        else:
            print("Ignore")

paths = ["/home/wr/some_file.txt", "/var/log/code.cpp",
"/opt.cpp/set/set.a12", "/optc/set/not_cpp", "/cpp/set/other.cpp",
"d:\winfiles\some.txt", "/home/alex/noextent", "/home/alex/Big.a15",
"/home/w/a.points.a.txt"] 

apply_exp(paths, r'\w+\.cpp$', "\n*** Looking for file with cpp extention ***\n")
apply_exp(paths, r'[a-zA-Z0-9_.]+$', "\n*** Extract any filename ***\n")

  

